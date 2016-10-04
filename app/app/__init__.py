import flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_swagger import swagger

app = flask.Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

CORS(app, resources=r'/*', allow_headers='*')


@app.route("/spec")
def spec():
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "Api boilerplate"
    swag['info']['description'] = "Api boilerplate for python flask based microservices"
    return flask.jsonify(swag)


@app.errorhandler(404)
def not_found(error):
    err = {'message': "Resource doesn't exist."}
    return flask.jsonify(**err)

# We need to import those blueprints, AFTER the initialization
# of both 'app', and 'db', this is why we are importing them
# here, and ignoring the E402 error.
from app.blog.resources import blog_bp  # noqa: E402
from app.pages.resources import page_bp  # noqa: E402

app.register_blueprint(
    blog_bp,
    url_prefix='/blog'
)

app.register_blueprint(
    page_bp,
    url_prefix='/page'
)

if app.config['DEBUG']:
    import newrelic.agent
    newrelic.agent.initialize('./newrelic.ini')
