class Status(object):
    '''
    Represents a Status object used by ExpressStatus resource.
    '''

    def __init__(self, subscription_status):
        self.subscription_status = subscription_status


class Product(object):
    '''
    Single product used in the 'products' list in Products
    '''
    def __init__(self, data):
        print data
        self.retry_periods = data.get('retry_periods', None)
        self.visible = data.get('visible', None)
        self.local_display_price = data.get('local_display_price', None)
        self.payment_method = data.get('payment_method', None)
        self.display_subscription_length = data.get('display_subscription_length', None)
        self.country_restrictions = data.get('country_restrictions', None)
        self.uuid = data.get('uuid', None)
        self.local_price = data.get('local_price', None)
        self.priority = data.get('priority', None)
        self.subscription_length = data.get('subscription_length', None)
        self.internal_name = data.get('internal_name', None)
        self.description_texts = data.get('description_texts', None)
        self.bundled = data.get('bundled', None)
        self.display_price = data.get('display_price', None)
        self.price = data.get('price', None)
        self.local_currency = data.get('local_currency', None)
        self.client_meta = data.get('client_meta', None)
        self.apply_coupon_code = data.get('apply_coupon_code', None)
        self.apply_pizza_code = data.get('apply_pizza_code', None)
        self.fallback_product = data.get('fallback_product', None)
        self.currency = data.get('currency', None)
        self.apply_cancellation_code = data.get('apply_cancellation_code', None)


class Products(object):
    '''
    Represents a Products object used by ExpressProducts resource.
    '''

    def __init__(self, country, banner_url, mobile_banner_url, icon_url, products):
        self.country = country
        self.banner_url = banner_url
        self.mobile_banner_url = mobile_banner_url
        self.icon_url = icon_url

        self.products = list(map(lambda p: Product(p), products))
