from .base import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    #('admin1', 'my@email.com'),
)

MANAGERS = ADMINS

DASHBOARD_PROJECT_NAME = 'nodeshot'
DASHBOARD_GITHUB = {
    'user': 'user',
    'repo': 'repo',
    'token': 'token'
}

DASHBOARD_MAILING_LIST = {
    'url': 'url/members',
    'password': 'password',
    'verify_ssl': False
}

INFLUXDB_HOST = 'localhost'
INFLUXDB_PORT = '8086'
INFLUXDB_USER = 'root'
INFLUXDB_PASSWORD = 'root'
INFLUXDB_DATABASE = '%s-dashboard' % DASHBOARD_PROJECT_NAME
