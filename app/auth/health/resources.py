from datetime import datetime

from flask import Blueprint, request, abort
from flask_restful import Api, Resource, fields, marshal_with

from auth import app
from auth.common.services.http import HttpError
from auth.common.services.oauth import OauthService
from auth.common.services.products import ProductsService
from auth.common.services.sms import SmsService
from auth.health.forms import HealthForm
from auth.health.models import Health

health_bp = Blueprint('health_api', __name__)
api = Api(health_bp)

health_fields = {
    'status': fields.String,
    'environment': fields.String,
    'application': fields.String,
    'timestamp': fields.DateTime(dt_format='iso8601')
}


def make_health_model(status):
    return Health(
        status,
        app.config['ENVIRONMENT'],
        app.config['APP_NAME'],
        datetime.now()
    )


class HealthDetails(Resource):
    oauth_service = OauthService()
    sms_service = SmsService()
    products_service = ProductsService()

    @marshal_with(health_fields)
    def get(self):
        """
        Health check on the app itself and its dependencies
        ---
        definitions:
        - schema:
            id: Health
            properties:
                status:
                    type: string
                    description: message about the status
                environment:
                    type: string
                    description: app's environment
                application:
                    type: string
                    description: app's name
                timestamp:
                    type: string
                    format: date-time
                    description: current timetamp
        responses:
            200:
                description: All services up and running
                schema:
                    $ref: '#/definitions/Health'
            401:
                description: The application's token is missing or invalid
            500:
                description: At least one service or the app itself is down
                schema:
                    $ref: '#/definitions/Health'
        parameters:
        - name: token
          in: query
          description: application's token
          required: true
          type: string
        """
        form = HealthForm(request.args)
        if not form.validate():
            abort(401, form.errors)

        try:
            self.oauth_service.health()
        except HttpError:
            return make_health_model("oauth down"), 500

        try:
            self.sms_service.health()
        except HttpError:
            return make_health_model("sms gateway down"), 500

        try:
            self.products_service.health()
        except HttpError:
            return make_health_model("products down"), 500

        # TODO: Billing and User profile APIs do not have a /health
        # Source: https://github.com/icflix-hub/auth/issues/6

        return make_health_model("ok")


api.add_resource(HealthDetails, '/')
