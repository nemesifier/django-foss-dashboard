import httplib2

from googleapiclient.discovery import build
from googleapiclient.http import HttpError
from oauth2client.client import SignedJwtAssertionCredentials


def get_metrics(certificate_path, service_account_email_address, profile_id, date):
    """
    credits: http://chriskief.com/2014/11/05/google-analytics-api-using-python-and-a-service-account/
    """
    # load the service account key
    # this key is managed here - https://console.developers.google.com/project
    filename = certificate_path
    f = file(filename, 'rb')
    key = f.read()
    f.close()

    # create the credentials
    credentials = SignedJwtAssertionCredentials(service_account_email_address, key, scope='https://www.googleapis.com/auth/analytics.readonly')

    # authorize the http instance with these credentials
    http = httplib2.Http()
    http = credentials.authorize(http)

    # construct a resource object for interacting with an api
    service = build('analytics', 'v3', http=http)

    # build the query
    # your profile id can be found by heading to google analytics, selecting your profile, clicking the admin button,
    # and then clicking view settings under the view column, the id is labelled 'View ID'
    # you can see the available metrics here:
    # https://developers.google.com/analytics/devguides/reporting/core/dimsmets
    api_query = service.data().ga().get(
        ids='ga:%s' % profile_id,
        metrics='ga:users, ga:sessions, ga:avgSessionDuration, ga:pageviews, ga:pageviewsPerSession, ga:percentNewSessions, ga:bounceRate',
        start_date=date,
        end_date=date
    )

    # default value
    metrics = None

    # run it
    try:
        result = api_query.execute()
        values = result['rows'][0]

        # the order below is the same as the order the metrics were listed above
        metrics = {
            'users': int(values[0]),
            'sessions': int(values[1]),
            'avg_session': float('{0:.2f}'.format(float(values[2]))),
            'pageviews': int(values[3]),
            'pages_session': float('{0:.2f}'.format(float(values[4]))),
            'new_sessions': float('{0:.2f}'.format(float(values[5]))),
            'returning_sessions': 100 - float('{0:.2f}'.format(float(values[5]))),
            'bounce_rate': float('{0:.2f}'.format(float(values[6])))
        }

    # handle errors in constructing a query
    except TypeError, error:
        print ('There was an error in constructing your query : %s' % error)

    # handle api service errors
    except HttpError, error:
        print ('There was an API error : %s : %s' % (error.resp.status, error._get_reason()))

    return metrics
