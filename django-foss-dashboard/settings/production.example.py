from .base import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    #('admin1', 'my@email.com'),
)

MANAGERS = ADMINS

DASHBOARD_PROJECT_NAME = 'nodeshot'

INFLUXDB_HOST = 'localhost'
INFLUXDB_PORT = '8086'
INFLUXDB_USER = 'root'
INFLUXDB_PASSWORD = 'root'
INFLUXDB_DATABASE = '%s-dashboard' % DASHBOARD_PROJECT_NAME

DASHBOARD_GITHUB = {
    'user': 'user',
    'repo': 'repo',
}

DASHBOARD_MAILMAN2 = {
    'url': 'url/members',
    'password': 'password',
    'verify_ssl': False
}
