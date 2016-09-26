import flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_restful import abort
from flask_migrate import Migrate
from flask_cors import CORS

app = flask.Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

CORS(app, resources=r'/*', allow_headers='*')

@app.errorhandler(404)
def not_found(error):
    err = {'message': "Resource doesn't exist."}
    return flask.jsonify(**err)


from app.blog.resources import blog_bp
from app.pages.resources import page_bp

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
