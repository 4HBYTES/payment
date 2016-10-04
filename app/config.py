import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = os.environ.get('DEBUG', True)

SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite'))
DATABASE_CONNECT_OPTIONS = {}
SQLALCHEMY_TRACK_MODIFICATIONS = False

THREADS_PER_PAGE = 2

SECRET_KEY = os.environ.get('SECRET_KEY', '9oup6z5mdbw)8(f5$9ob@m&xha*(5ulqot&x*y1n$1^^9qo#d-')

NEW_RELIC_CONFIG_FILE = 'newrelic.ini newrelic-admin run-program command options'
