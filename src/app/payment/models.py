'''
Models
'''


class Product(object):
    '''
    Product definition from the CMS
    '''

    def __init__(self, data):
        self.id = data.get('id', '')
        self.name = data.get('name', '')
        self.price = data.get('price', 1.0)
        self.currency = data.get('currency', 'USD')
