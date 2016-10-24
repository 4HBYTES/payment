import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = os.environ.get('DEBUG', True)

THREADS_PER_PAGE = 2

ERROR_404_HELP = False

SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite'))
DATABASE_CONNECT_OPTIONS = {}
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = os.environ.get('SECRET_KEY', '9oup6z5mdbw)8(f5$9ob@m&xha*(5ulqot&x*y1n$1^^9qo#d-')

NEW_RELIC_CONFIG_FILE = 'newrelic.ini newrelic-admin run-program command options'

APP_NAME = os.environ.get('APP_NAME', 'flask-boilerplate')

ENVIRONMENT = os.environ.get('ENVIRONMENT', 'staging')

APP_TOKEN = os.environ.get('APP_TOKEN', '4b6f204b-04e8-489a-9aec-7d204e4cec34')
