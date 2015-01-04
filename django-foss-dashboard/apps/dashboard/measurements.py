import re
import json
import requests

from influxdb_metrics.utils import write_point, write_points, query
from influxdb.client import InfluxDBClientError
from django.conf import settings


def store_github_repo_stats():
    """ collect metrics from a public github repository """
    url = 'https://api.github.com/repos/{user}/{repo}'.format(user=settings.DASHBOARD_GITHUB['user'],
                                                                  repo=settings.DASHBOARD_GITHUB['repo'])
    response = requests.get(url)
    data = json.loads(response.content)
    # get contributors count
    response = requests.get('{url}/contributors'.format(url=url))
    data['contributors'] = len(json.loads(response.content))

    github_api_key_map = {
        'stars': 'stargazers_count',
        'forks': 'forks_count',
        'watchers': 'subscribers_count',
        'issues': 'open_issues_count',
        'size': 'size',
        'contributors': 'contributors'
    }

    for metric_name, github_api_attribute in github_api_key_map.items():
        # get current total count
        total = data[github_api_attribute]
        # get last count
        try:
            last = query('SELECT total FROM github.%s LIMIT 1' % metric_name)[0]['points'][0][2]
        except InfluxDBClientError:
            last = total
        # calculate difference
        difference = total - last
        # write
        write_points([
            {
                'name': 'github.%s' % metric_name,
                'columns': ['total', 'difference'],
                'points': [[total, difference]]
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
    # convert to integer
    total = int(subscribers)
    # get last subscribers count
    try:
        last = query('SELECT subscribers FROM mailing_list LIMIT 1')[0]['points'][0][2]
    except InfluxDBClientError:
        last = total
    # calculate difference
    difference = total - last
    # store count
    write_points([
        {
            'name': 'mailing_list',
            'columns': ['total', 'difference'],
            'points': [[total, difference]]
        }
    ])
