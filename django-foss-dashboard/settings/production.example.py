from .base import *


ADMINS = (
    #('admin1', 'my@email.com'),
)

MANAGERS = ADMINS

DASHBOARD_PROJECT_NAME = 'myproject'

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
    'verify_ssl': True
}

DASHBOARD_GOOGLE_ANALYTICS = [
    {
        'series-name': 'ga-myproject',
        'certificate_path': '/path/to/myproject.p12',
        'service_account_email_address': 'myproject@developer.gserviceaccount.com',
        'profile_id': 'GA_PROFILE_ID'
    }
]
