from flask import Blueprint, request, abort
from flask_restful import Api, Resource, fields, marshal_with

from auth.common.services.http import HttpError
from auth.common.services.products import ProductsService
from auth.products.models import Products

products_bp = Blueprint('products_api', __name__)
api = Api(products_bp)

product_fields = {
    'uuid': fields.String,
    'local_display_price': fields.Float,
    'display_subscription_length': fields.Integer,
    'local_price': fields.Float,
    'subscription_length': fields.Integer,
    'description_texts': fields.String,
    'display_price': fields.Float,
    'price': fields.Float,
    'local_currency': fields.String,
    'currency': fields.String
}

products_fields = {
    'country': fields.String,
    'banner_url': fields.String,
    'mobile_banner_url': fields.String,
    'icon_url': fields.String,
    'products': fields.Nested(product_fields)
}


class ProductsResource(Resource):
    products_service = ProductsService()

    @marshal_with(products_fields)
    def get(self, telco, product_id=None):
        """
        Returns telcos information and available products, will filter the product if set
        ---
        definitions:
        - schema:
            id: ExpressProduct
            properties:
                uuid:
                    type: string
                    description: product identifier
                    format: uuid
                local_display_price:
                    type: number
                    description: local price
                    format: float
                display_subscription_length:
                    type: number
                    description: number of days
                local_price:
                    type: number
                    description: local price
                    format: float
                subscription_length:
                    type: number
                    description: number of days
                description_texts:
                    type: string
                    description: descriptions for different languages
                display_price:
                    type: number
                    description: original price
                    format: float
                price:
                    type: number
                    description: original price
                    format: float
                local_currency:
                    type: string
                    description: local currency
                currency:
                    type: string
                    description: original currency
        - schema:
            id: ExpressProducts
            properties:
                country:
                    type: string
                    description: 2 letters ISO country code
                banner_url:
                    type: string
                    description: URL to the telco's banner
                mobile_banner_url:
                    type: string
                    description: URL to the telco's mobile banner
                icon_url:
                    type: string
                    description: URL to the telco's icon
                products:
                    type: array
                    description: List of available products
                    items:
                        $ref: '#/definitions/ExpressProduct'
        responses:
            200:
                description: telco's details and available products
                schema:
                    $ref: '#/definitions/ExpressProducts'
            404:
                description: could not find the telco, or it is not sms
                    recurrent, or it does not support direct billing.
            500:
                description: could not access the products API
        parameters:
        - name: telco
          in: path
          description: telco supporting direct billing
          required: true
          type: string
        - name: product_id
          in: path
          description: product UUID to filter
          required: true
          type: string
        """
        # TODO: There is a small swagger problem with path parameters,
        # see: https://github.com/gangverk/flask-swagger/issues/37

        # TODO: Is this actually going to work on the new infra ?
        country = request.headers.get('HTTP_ICFLIX_INT_COUNTRY', 'AE')
        platform = request.headers.get('icflix-int-Platform', 'website')

        try:
            response = self.products_service. \
                get_payment_methods_by_country_and_platform(country, platform)
        except HttpError as e:
            abort(503, e.message)

        payment_methods = response['payment_methods']
        payment_method = next(
            (p for p in payment_methods if p['payment_method'] == telco),
            None)

        if payment_method is None:
            abort(404, "cannot find telco")

        is_sms_recurrent = payment_method['payment_class'] == 'sms_recurrent'

        if not is_sms_recurrent:
            abort(404, "telco is not sms recurrent")

        client_meta = payment_method.get('client_meta', False)
        is_supported = client_meta and client_meta.get('can_request_code', False)

        if not is_supported:
            abort(404, "telco does not support direct billing")

        products = payment_method['products']
        product = None
        if product_id:
            product = next((p for p in products if p['uuid'] == product_id), None)

        return Products(
            country,
            payment_method['banner_url'],
            payment_method['mobile_banner_url'],
            payment_method['express_icon_url'],
            [product] if product else products)


api.add_resource(ProductsResource, '/<string:telco>', '/<string:telco>/<string:product_id>')
