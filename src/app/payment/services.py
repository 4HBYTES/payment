'''
TODO
'''
from app import app, db
from app.payment.models import Product, Order
import paypalrestsdk
import requests
from datetime import datetime


class OrderService(object):
    '''
    Database wrapper for the orders
    '''

    def _create_order(self, paypal_payment_id, user_id, product_id, quantity, status):
        '''
        Private method to create an order
        '''
        order = Order({
            'paypal_payment_id': paypal_payment_id,
            'user_id': user_id,
            'product_id': product_id,
            'quantity': quantity,
            'created_at': datetime.now(),
            'status': status
        })

        db.session.add(order)
        db.session.commit()

    def create_init_order(self, paypal_payment_id, user_id, product_id, quantity):
        '''
        Create an order with the 'init' status
        '''
        self._create_order(paypal_payment_id, user_id, product_id, quantity, 'init')

    def create_failed_order(self, paypal_payment_id, user_id, product_id, quantity):
        '''
        Create an order with the 'failed' status
        '''
        self._create_order(paypal_payment_id, user_id, product_id, quantity, 'fail')

    def create_success_order(self, paypal_payment_id, user_id, product_id, quantity):
        '''
        Create an order with the 'success' status
        '''
        self._create_order(paypal_payment_id, user_id, product_id, quantity, 'success')

    def get_order_by_payment_id(self, payment_id):
        '''
        Returns an order by paypal_payment_id
        '''
        return Order.query\
            .filter_by(paypal_payment_id=payment_id)\
            .first()


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
