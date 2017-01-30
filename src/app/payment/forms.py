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
