import flask
from flask_cors import CORS
from flask_restplus import Api
from app.logger import ContextualFilter, handler
import paypalrestsdk

app = flask.Flask(__name__)
app.config.from_object('config')

app.logger.addFilter(ContextualFilter())
app.logger.addHandler(handler)

CORS(app, resources=r'/*', allow_headers='*')

paypalrestsdk.configure({
    'mode': app.config['PAYPAL_MODE'],
    'client_id': app.config['PAYPAL_CLIENT_ID'],
    'client_secret': app.config['PAYPAL_CLIENT_SECRET']
})


@app.errorhandler(404)
def not_found(error):
    err = {'message': "Resource doesn't exist."}
    return flask.jsonify(**err), 404


@app.errorhandler(500)
def internal_error(error):
    err = {'message': "Internal server error"}
    return flask.jsonify(**err), 500


@app.after_request
def after_request(response):
    '''
    Currently logging every single request
    '''
    # TODO: Weird, https://github.com/pallets/flask/issues/993
    response.direct_passthrough = False

    app.logger.info(
        response.status,
        extra={
            'response': response.data.replace('\n', '').replace('    ', ''),
            'status_code': response.status_code
        }
    )
    return response

# We need to import those blueprints, AFTER the initialization
# of both 'app', and 'db', this is why we are importing them
# here, and ignoring the E402 error.


from app.health.resources import ns as health_ns  # noqa: E402
from app.payment.resources import ns as payment_ns  # noqa: E402

api = Api(
    app,
    version='1.0',
    title='Payment API',
    description='Payment API description',
    doc=False
)
api.add_namespace(health_ns)
api.add_namespace(payment_ns)

if app.config['DEBUG'] and app.config['ENVIRONMENT'] != 'testing':
    import rollbar
    import rollbar.contrib.flask
    import json
    from flask import got_request_exception

    rollbar.init(
        app.config['ROLLBAR_ACCESS_TOKEN'],
        app.config['ENVIRONMENT'],
        root=app.config['BASE_DIR'],
        allow_logging_basic_config=False
    )
    got_request_exception.connect(rollbar.contrib.flask.report_exception, app)

    @app.route('/spec/')
    def spec():
        return json.dumps(api.__schema__)
