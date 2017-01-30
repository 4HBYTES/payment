from flask import request, abort
from flask_restplus import Resource, fields, Namespace

from app.payment.forms import InitForm
from app.payment.services import PaypalService, ProductService

ns = Namespace('payment', description='Payment module')

paypal_init_input = ns.model('Payment', {
    'product': fields.String(description='Product UUID'),
    'quantity': fields.Integer(description='Quantity of product')
})

# TODO
paypal_init_output = ns.model('Payment', {
})


@ns.route('/paypal/init')
class PaypalPayment(Resource):

    paypal_service = PaypalService()
    product_service = ProductService()

    @ns.doc('paypal_init')
    @ns.expect(paypal_init_input)
    @ns.response(500, 'shit is broken')
    @ns.marshal_with(paypal_init_output)
    def post(self):
        '''
        TODO
        '''

        # Retrieves the payload as json, failure will trigger
        # automatically a 400 with the following message :
        # Failed to decode JSON object: No JSON object could be decoded
        data = request.get_json(force=True)

        form = InitForm(data=data)
        if not form.validate():
            abort(401, form.errors)

        product = self.product_service.get_product(
            form.data['product']
        )

        # TODO: 404 cannot find the product

        payment = self.paypal_service.create_payment(
            product,
            form.data['quantity']
        )
        if not payment.create():
            abort(500, payment.error)

        for link in payment.links:
            if link.method == "REDIRECT":
                redirect_url = str(link.href)
                return redirect_url, 302

        abort(500, 'No redirect link found')
