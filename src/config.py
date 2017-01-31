import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = os.environ.get('DEBUG', True)

THREADS_PER_PAGE = 2

ERROR_404_HELP = False

RESTPLUS_MASK_SWAGGER = False

SQLALCHEMY_DATABASE_URI = os.environ.get(
    'SQLALCHEMY_DATABASE_URI',
    'postgresql://payment:payment@localhost:5432/payment'
)
DATABASE_CONNECT_OPTIONS = {}
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = os.environ.get('SECRET_KEY', '0(=pxgxx#k+qot@a1xc4$(c$h!-v_^^*uf_04*90bt4eqe7@pf')

APP_NAME = os.environ.get('APP_NAME', 'payment-billing')

ENVIRONMENT = os.environ.get('ENVIRONMENT', 'staging')

APP_TOKEN = os.environ.get('APP_TOKEN', '1c46c050-9058-4a7c-ae60-ce6bb02582b5')

ROLLBAR_ACCESS_TOKEN = os.environ.get('ROLLBAR_ACCESS_TOKEN', 'TO_SET')

PAYPAL_MODE = os.environ.get('PAYPAL_MODE', 'sandbox')
PAYPAL_CLIENT_ID = os.environ.get('PAYPAL_CLIENT_ID', 'TODO')
PAYPAL_CLIENT_SECRET = os.environ.get('PAYPAL_CLIENT_SECRET', 'TODO')
PAYPAL_RETURN_URL = os.environ.get('PAYPAL_RETURN_URL', 'http://127.0.0.1:5000/payment/paypal/progress')
PAYPAL_CANCEL_URL = os.environ.get('PAYPAL_CANCEL_URL', 'https://baidu.com')
PAYPAL_SUCCESS_URL = os.environ.get('PAYPAL_SUCCESS_URL', 'https://baidu.com?sucess=true')
PAYPAL_FAILURE_URL = os.environ.get('PAYPAL_FAILURE_URL', 'https://baidu.com?success=false')
PAYPAL_TRANSACTION_DESCRIPTION = os.environ.get('PAYPAL_TRANSACTION_DESCRIPTION', 'Paypal description')

CMS_API = os.environ.get('CMS_API', 'http://127.0.0.1:8000')
CMS_APP_TOKEN = os.environ.get('CMS_APP_TOKEN', '3d008cb7-15ce-4e30-b5d1-b626064797fc')
