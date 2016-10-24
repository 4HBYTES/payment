from auth import app
from auth.common.services.http import make_query


class ProductsService(object):
    """
    Service to wrap the access to the Products API
    """

    def get_payment_methods_by_country_and_platform(self, country, platform):
        """
        Calls the endpoint payment_methods/{country}/{platform}
        Source: not documented ?
        Returns the json parsed response or raise an HTTP error
        """
        url = app.config['PRODUCTS_API'] + 'payment_methods/{}/{}'.format(country, platform)
        return make_query('get', url)

    def health(self):
        """
        Calls the endpoint health
        Source: not documented
        Returns the json parsed response or raise an HTTP error
        """
        url = app.config['PRODUCTS_API'] + 'health'
        return make_query('get', url)
