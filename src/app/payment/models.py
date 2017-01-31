'''
Models
'''
from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Product(object):
    '''
    Product definition from the CMS
    '''

    def __init__(self, data):
        self.id = data.get('id', '')
        self.name = data.get('name', '')
        self.price = data.get('price', 1.0)
        self.currency = data.get('currency', 'USD')


class Order(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    paypal_payment_id = db.Column(db.String(100))
    user_id = db.Column(db.String(100))
    product_id = db.Column(db.String(100))
    quantity = db.Column(db.Float())
    created_at = db.Column(db.DateTime())
    status = db.Column(db.String(100))

    def __init__(self, data):
        self.paypal_payment_id = data['paypal_payment_id']
        self.user_id = data['user_id']
        self.product_id = data['product_id']
        self.quantity = data['quantity']
        self.created_at = data['created_at']
        self.status = data['status']
