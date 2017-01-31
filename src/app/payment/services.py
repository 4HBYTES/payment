'''
TODO
'''
from app import app
from app.payment.models import Product
import paypalrestsdk
import requests


class ProductService(object):
    '''
    HTTP wrapper to the CMS
    '''

    def get_product(self, uuid):
        '''
        Returns a product by uuid
        '''
        url = '{}/products/{}'.format(
            app.config['CMS_API'],
            uuid
        )
        response = requests.get(url)
        return Product(response.json())


class PaypalService(object):
    '''
    TODO
    '''

    def create_payment(self, product, quantity):
        '''
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
            'transactions': [{
                'item_list': {
                    'items': [{
                        'name': product.name,
                        'sku': product.id,
                        'price': str(product.price),
                        'currency': product.currency,
                        'quantity': quantity
                    }]
                },
                'amount': {
                    'total': str(product.price * quantity),
                    'currency': product.currency
                },
                'description': app.config['PAYPAL_TRANSACTION_DESCRIPTION']
            }]
        })

    def get_payment(self, payment_id):
        '''
        Returns the payment object corresponding to the ID
        '''
        return paypalrestsdk.Payment.find(payment_id)
