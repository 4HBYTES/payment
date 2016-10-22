import flask
from flask_cors import CORS
from flask_swagger import swagger
from logger import ContextualFilter, handler, logentry_handler

app = flask.Flask(__name__)
app.config.from_object('config')

app.logger.addFilter(ContextualFilter())
app.logger.addHandler(handler)
app.logger.addHandler(logentry_handler)

CORS(app, resources=r'/*', allow_headers='*')


@app.route("/spec")
def spec():
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "Auth"
    swag['info']['description'] = "Micro service in charge of signup/signin"
    return flask.jsonify(swag)


@app.after_request
def after_request(response):
    '''
    Currently logging every single request, except non failing /health/
    '''
    if flask.request.path == '/health/' and response.status_code == 200:
        return response

    app.logger.info(
        response.status,
        extra={
            'response': response.data.replace('\n', '').replace('    ', ''),
            'status_code': response.status_code
        }
    )
    return response


# We need to import those blueprints, AFTER the initialization
# of 'app', this is why we are importing them here,
# and ignoring the Flake8 error.
from auth.health.resources import health_bp  # noqa: E402
from auth.user.resources import user_bp  # noqa: E402
from auth.products.resources import products_bp  # noqa: E402

app.register_blueprint(
    health_bp,
    url_prefix='/health'
)

app.register_blueprint(
    user_bp,
    url_prefix='/user'
)

app.register_blueprint(
    products_bp,
    url_prefix='/products'
)

if app.config['DEBUG']:
    import newrelic.agent
    newrelic.agent.initialize('./newrelic.ini')
