from datetime import datetime

from flask import request, abort
from flask_restplus import Resource, fields, Namespace

from app import app
from app.health.forms import HealthForm
from app.health.models import Health

ns = Namespace('health', description='Health module')

health_fields = ns.model('Health', {
    'status': fields.String(description='message about the status'),
    'environment': fields.String(description='app\'s environment'),
    'application': fields.String(description='app\'s name'),
    'timestamp': fields.DateTime(dt_format='iso8601', description='current timestamp')
})


def make_health_model(status):
    return Health(
        status,
        app.config['ENVIRONMENT'],
        app.config['APP_NAME'],
        datetime.now()
    )


@ns.route('/')
class HealthDetails(Resource):

    @ns.doc('get_health', params={'token': 'Application\'s token'})
    @ns.response(401, 'The application\'s token is missing or invalid')
    @ns.response(500, 'At least one service or the app itself is down')
    @ns.marshal_with(health_fields)
    def get(self):
        """
        Health check on the app itself and its dependencies
        """
        form = HealthForm(request.args)
        if not form.validate():
            abort(401, form.errors)

        # TODO: implement here the logic for health

        return make_health_model("ok")
