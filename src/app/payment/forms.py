'''
TODO
'''
from wtforms import Form, StringField, IntegerField, validators


class InitForm(Form):
    '''
    TODO
    '''
    # TODO: Make sure it's >1 and <99 (for instance)
    quantity = IntegerField('quantity', [validators.required()])
    product = StringField('product', [validators.required()])
    user_id = StringField('user_id', [validators.required()])


class PaypalProgressForm(Form):
    '''
    Callback: GET ?paymentId=PAY-1UJ52767AT248112ELCHR7NY&token=EC-0LD50166GX320414D&PayerID=93YXES9UBG7J6
    '''
    paymentId = StringField('payment_id', [validators.required()])
    token = StringField('token', [validators.required()])
    PayerID = StringField('payer_id', [validators.required()])
