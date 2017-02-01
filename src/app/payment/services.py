'''
TODO
'''
from app import app, db
from app.payment.models import Product, Order, ProductOrder
import paypalrestsdk
import requests
from datetime import datetime


class OrderService(object):
    '''
    Database wrapper for the orders
    '''

    def _create_order(self, paypal_payment_id, user_id, products, order_id, status):
        '''
        Private method to create an order
        '''
        order = Order({
            'paypal_payment_id': paypal_payment_id,
            'user_id': user_id,
            'created_at': datetime.now(),
            'status': status
        })

        db.session.add(order)
        db.session.commit()

        if status != 'init':
            order.parent_id = order_id
            db.session.add(order)
            db.session.commit()
            return

        order.parent_id = order.id

        db.session.add(order)

        for item in products:
            product_order = ProductOrder({
                'product_id': item['product'].id,
                'quantity': item['quantity'],
                'order_id': order.id
            })
            db.session.add(product_order)

        db.session.commit()

    def create_init_order(self, paypal_payment_id, user_id, products):
        '''
        Create an order with the 'init' status
        '''
        self._create_order(paypal_payment_id, user_id, products, None, 'init')

    def create_failed_order(self, paypal_payment_id, user_id, order_id):
        '''
        Create an order with the 'failed' status
        '''
        self._create_order(paypal_payment_id, user_id, None, order_id, 'fail')

    def create_success_order(self, paypal_payment_id, user_id, order_id):
        '''
        Create an order with the 'success' status
        '''
        self._create_order(paypal_payment_id, user_id, None, order_id, 'success')

    def get_order_by_payment_id(self, payment_id):
        '''
        Returns an order by paypal_payment_id
        '''
        return Order.query\
            .filter_by(paypal_payment_id=payment_id)\
            .first()


class CmsService(object):
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

    def create_tickets(self, order):
        '''
        Create tickets
        '''
        products = []
        for item in order.product_orders:
            products.append({
                'product_id': item.product_id,
                'quantity': item.quantity
            })

        data = {
            'token': app.config['CMS_APP_TOKEN'],
            'products': products,
            'user_id': order.user_id
        }
        url = '{}/ticket/create'.format(
            app.config['CMS_API']
        )
        requests.post(url, json=data)


class PaypalService(object):
    '''
    TODO
    '''

    def create_payment(self, products):
        '''
        Sample here: https://github.com/paypal/PayPal-Python-SDK/blob/master/samples/payment/create_with_paypal.py
        '''
        items = []
        total = 0
        currency = products[0]['product'].currency

        for item in products:
            product = item['product']
            quantity = int(item['quantity'])

            items.append({
                'name': product.name,
                'sku': product.id,
                'price': str(product.price),
                'currency': product.currency,
                'quantity': quantity
            })
            total += product.price * quantity

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
                    'items': items
                },
                'amount': {
                    'total': str(total),
                    'currency': currency
                },
                'description': app.config['PAYPAL_TRANSACTION_DESCRIPTION']
            }]
        })

    def get_payment(self, payment_id):
        '''
        Returns the payment object corresponding to the ID
        '''
        return paypalrestsdk.Payment.find(payment_id)
