import re
import json
import requests
from collections import OrderedDict

from influxdb_metrics.utils import write_point, write_points
from django.conf import settings


def store_github_repo_stats(dummy=False):
    columns = OrderedDict((
        ('stars', 'stargazers_count'),
        ('forks', 'forks_count'),
        ('watchers', 'subscribers_count'),
        ('issues', 'open_issues_count'),
        ('size', 'size')
    ))

    if not dummy:
        url = 'https://api.github.com/repos/{user}/{repo}'.format(user=settings.DASHBOARD_GITHUB['user'],
                                                                  repo=settings.DASHBOARD_GITHUB['repo'])
        response = requests.get(url)
        data = json.loads(response.content)
        values = [data[api_attribute] for api_attribute in columns.values()]
    else:
        values = [0] * len(columns.values())

    # get contributors count
    columns['contributors'] = 'contributors'

    if not dummy:
        response = requests.get('{url}/contributors'.format(url=url))
        data = json.loads(response.content)
        values.append(len(data))  # length of the contributors list
    else:
        values.append(0)

    write_points([
        {
            'name': 'github.public.total',
            'columns': columns.keys(),
            'points': [values]
        }
    ])


def store_mailman2_list_subscribers():
    """ works for mailman v2 only """
    url = settings.DASHBOARD_MAILMAN2['url']
    password = settings.DASHBOARD_MAILMAN2['password']
    verify_ssl = bool(settings.DASHBOARD_MAILMAN2['verify_ssl'])
    # get members page
    response = requests.post(url, { 'adminpw': password, 'admlogin': '' }, verify=verify_ssl)
    # look for total subscribers
    regexp = re.compile('<em.*?>(.+?) members total</em>')
    subscribers = re.findall(regexp, response.content)[0]
    count = int(subscribers)
    # store count
    write_point('mailing_list.total', 'subscribers', count)
