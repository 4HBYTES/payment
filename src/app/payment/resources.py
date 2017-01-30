from flask import request, abort, redirect
from flask_restplus import Resource, fields, Namespace

from app.payment.forms import InitForm, PaypalProgressForm
from app.payment.services import PaypalService, ProductService
from app.logentries_logger import logger
from app import app

ns = Namespace('payment', description='Payment module')

paypal_init_input = ns.model('PaypalInit', {
    'product': fields.String(description='Product UUID'),
    'quantity': fields.Integer(description='Quantity of product')
})

# TODO
paypal_progress_input = {
    'paymentId': 'Payment ID provided by Paypal',
    'token': 'Token provided by Paypal',
    'PayerID': 'Payer ID provided by Paypal'
}


@ns.route('/paypal/init')
class PaypalCreatePayment(Resource):
    '''
    Create the payment in paypal's system.
    '''

    paypal_service = PaypalService()
    product_service = ProductService()

    @ns.doc('paypal_init')
    @ns.expect(paypal_init_input)
    @ns.response(400, 'Invalid input')
    @ns.response(500, 'shit is broken')
    def post(self):
        '''
        Should be called by the client to be redirected to paypal website.
        It will handle the user account and payment pre-approval.
        '''

        # Retrieves the payload as json, failure will trigger
        # automatically a 400 with the following message :
        # Failed to decode JSON object: No JSON object could be decoded
        data = request.get_json(force=True)

        form = InitForm(data=data)
        if not form.validate():
            abort(400, form.errors)

        product = self.product_service.get_product(
            form.data['product']
        )

        # TODO: 404 cannot find the product

        payment = self.paypal_service.create_payment(
            product,
            form.data['quantity']
        )
        if not payment.create():
            logger.error({
                'message': 'Could not create payment',
                'method': 'paypal',
                'context': payment.error
            })
            abort(500, payment.error)

        for link in payment.links:
            if link.method == "REDIRECT":
                redirect_url = str(link.href)
                logger.info({
                    'message': 'Success, redirecting user',
                    'method': 'paypal',
                    'context': link
                })
                return redirect(redirect_url, code=302)

        logger.error({
            'message': 'Could not find a redirection link',
            'method': 'paypal',
            'context': payment.links
        })
        abort(500, 'No redirect link found')


@ns.route('/paypal/progress')
class PaypalExecutePayment(Resource):
    '''
    Execute paypal pre-approved payment.
    '''

    paypal_service = PaypalService()

    @ns.doc('paypal_progress', params=paypal_progress_input)
    @ns.response(400, 'Invalid input')
    @ns.response(500, 'shit is broken')
    def get(self):
        '''
        Callback only for Paypal.
        It will execute the pre-approved payment and redirect the
        user to a website based on the payment success or failure.
        '''
        form = PaypalProgressForm(request.args)

        if not form.validate():
            logger.info({
                'message': 'Progress callback invalid',
                'method': 'paypal',
                'context': form.errors
            })
            abort(401, form.errors)

        payment = self.paypal_service.get_payment(
            form.data['paymentId']
        )

        if not payment.execute({"payer_id": form.data['PayerID']}):
            logger.error({
                'message': 'Payment failed',
                'method': 'paypal',
                'context': payment.error
            })
            return redirect(app.config['PAYPAL_FAILURE_URL'], code=302)

        logger.info({
            'message': 'Payment successful',
            'method': 'paypal',
            'context': payment.id
        })

        # TODO: From here probably send the tickets by email or
        # any kind of notifications to the user.

        return redirect(app.config['PAYPAL_SUCCESS_URL'], code=302)
