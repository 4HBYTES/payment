import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = os.environ.get('DEBUG', True)

THREADS_PER_PAGE = 2

SECRET_KEY = os.environ.get('SECRET_KEY', '9oup6z5mdbw)8(f5$9ob@m&xha*(5ulqot&x*y1n$1^^9qo#d-')

NEW_RELIC_CONFIG_FILE = 'newrelic.ini newrelic-admin run-program command options'

OAUTH_APP_TOKEN = os.environ.get('OAUTH_APP_TOKEN', '37ee02db-14e3-4303-a910-849ae94429de')

OAUTH_API = os.environ.get('OAUTH_API', 'https://secure.icflix.io/v12.16/oauth/')
