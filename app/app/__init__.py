import flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restplus import Api
from logger import ContextualFilter, handler, logentry_handler

app = flask.Flask(__name__)
app.config.from_object('config')

app.logger.addFilter(ContextualFilter())
app.logger.addHandler(handler)
app.logger.addHandler(logentry_handler)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

CORS(app, resources=r'/*', allow_headers='*')


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
from app.blog.resources import ns as blog_ns  # noqa: E402
from app.pages.resources import ns as pages_ns  # noqa: E402

doc = '/spec' if app.config['DEBUG'] else False
api = Api(
    app,
    version='1.0',
    title='Flask Api Boileplate',
    description='Example service',
    doc=doc
)
api.add_namespace(blog_ns)
api.add_namespace(pages_ns)

if app.config['DEBUG'] and app.config['ENVIRONMENT'] != 'testing':
    import rollbar
    import rollbar.contrib.flask
    from flask import got_request_exception

    rollbar.init(
        app.config['ROLLBAR_ACCESS_TOKEN'],
        app.config['ENVIRONMENT'],
        root=app.config['BASE_DIR'],
        allow_logging_basic_config=False
    )
    got_request_exception.connect(rollbar.contrib.flask.report_exception, app)
