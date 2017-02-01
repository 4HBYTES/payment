'''
TODO
'''
from wtforms import Form, StringField, IntegerField, validators, FieldList, FormField


class InitInnerForm(Form):
    '''
    TODO
    '''
    # TODO: Make sure it's >1 and <99 (for instance)
    quantity = IntegerField('quantity', [validators.required()])
    product = StringField('product', [validators.required()])


class InitForm(Form):
    products = FieldList(
        FormField(InitInnerForm),
        [validators.required()],
        min_entries=1
    )
    user_id = StringField('user_id', [validators.required()])


class PaypalProgressForm(Form):
    '''
    Callback: GET ?paymentId=PAY-1UJ52767AT248112ELCHR7NY&token=EC-0LD50166GX320414D&PayerID=93YXES9UBG7J6
    '''
    paymentId = StringField('payment_id', [validators.required()])
    token = StringField('token', [validators.required()])
    PayerID = StringField('payer_id', [validators.required()])
