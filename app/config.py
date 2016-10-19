import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = os.environ.get('DEBUG', True)

THREADS_PER_PAGE = 2

SECRET_KEY = os.environ.get('SECRET_KEY', '9oup6z5mdbw)8(f5$9ob@m&xha*(5ulqot&x*y1n$1^^9qo#d-')

NEW_RELIC_CONFIG_FILE = 'newrelic.ini newrelic-admin run-program command options'

OAUTH_APP_TOKEN = os.environ.get('OAUTH_APP_TOKEN', '37ee02db-14e3-4303-a910-849ae94429de')

OAUTH_API = os.environ.get('OAUTH_API', 'https://secure.icflix.io/v12.16/oauth/')
BILLING_API = os.environ.get('BILLING_API', 'https://api.icflix.io/v12.16/billing/')
USER_API = os.environ.get('USER_API', 'https://api.icflix.io/v12.16/user/')
SMS_API = os.environ.get('SMS_API', 'https://api.icflix.io/v12.16/sms/')
PRODUCTS_API = os.environ.get('PRODUCTS_API', 'https://icmoney-staging.icflix.com/api/')

APP_NAME = os.environ.get('APP_NAME', 'auth')

ENVIRONMENT = os.environ.get('ENVIRONMENT', 'staging')

APP_TOKEN = os.environ.get('APP_TOKEN', '053c4071-a683-4cbf-831d-394e6be95482')
