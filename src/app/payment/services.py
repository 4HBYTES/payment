'''
TODO
'''
from app import app
from app.payment.models import Product
import paypalrestsdk


class ProductService(object):
    '''
    TODO: This will probably be calling the CMS for
    product definition: retrieve price, etc
    '''

    def get_product(self, uuid):
        '''
        TODO: make actual call
        '''
        return Product({
            'uuid': uuid,
            'price': 10,
            'currency': 'USD',
            'name': 'Premium ticket'
        })


class PaypalService(object):
    '''
    TODO
    '''

    def create_payment(self, product, quantity):
        '''
        TODO: use a model, then to dict
        Sample here: https://github.com/paypal/PayPal-Python-SDK/blob/master/samples/payment/create_with_paypal.py
        '''
        return paypalrestsdk.Payment({
            'intent': 'sale',
            'payer': {
                'payment_method': 'paypal'
            },
            'redirect_urls': {
                'return_url': app.config['PAYPAL_RETURN_URL'],
                'cancel_url': app.config['PAYPAL_CANCEL_URL']
            },
            'transactions': {
                'item_list': {
                    'items': [{
                        'name': product.name,
                        'sku': 'test',  # TODO: no idea what's sku
                        'price': product.price,
                        'currency': product.currency,
                        'quantity': quantity
                    }]
                },
                'amount': {
                    'total': product.price * quantity,
                    'currency': product.currency
                },
                'description': app.config['PAYPAL_TRANSACTION_DESCRIPTION']
            }
        })

    def execute_payment(self):
        '''
        TODO
        '''
        pass

    def get_details(self):
        '''
        TODO
        '''
        pass
