'''
TODO
'''


class Product(object):
    '''
    TODO
    '''

    def __init__(self, data):
        self.uuid = data.get('uuid', '')
        self.name = data.get('name', '')
        self.price = data.get('price', 1)
        self.currency = data.get('currency', 'USD')
