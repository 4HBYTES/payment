from flask import Blueprint

from flask_restful import Api, Resource
from flask_restful import fields, marshal_with

from auth.common.services.http import HttpError
from auth.common.services.user import UserService
from auth.user.models import Status


user_bp = Blueprint('user_api', __name__)
api = Api(user_bp)

status_fields = {
    'subscription_status': fields.String
}


class UserStatusResource(Resource):
    user_service = UserService()

    @marshal_with(status_fields)
    def get(self, token):
        """
        Determines if the token is valid and returns the subscription status
        ---
        definitions:
        - schema:
            id: ExpressStatus
            properties:
                status:
                    type: string
                    description: can be none, basic or premium
        responses:
            200:
                description: subscription status related to the token
                schema:
                    $ref: '#/definitions/ExpressStatus'
        parameters:
        - name: token
          in: path
          description: user's token
          required: true
          type: string
        """
        try:
            response = self.user_service.get_current_profile(token)
            if response['subscription_status'] == "full":
                return Status('premium')
            else:
                return Status('basic')
        except HttpError:
            return Status('none')


api.add_resource(UserStatusResource, '/status/<string:token>')
