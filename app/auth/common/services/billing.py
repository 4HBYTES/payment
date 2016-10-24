from auth import app
from auth.common.services.http import make_query


class BillingService(object):
    """
    Service to wrap the access to the Billing API
    """

    def create_sms_instrument(self, msisdn, partner, product_code, lifetime=86400):
        """
        Calls the endpoint instruments/recurrent
        Source: https://api.icflix.com/doc/api/billing.html#method-create-sms-recurring
        Returns the json parsed response or raise an HTTP error
        """
        params = {
            'msisdn': msisdn,
            'partner': partner,
            'product_code': product_code,
            'lifetime': lifetime
        }
        headers = {'Authorization': 'Bearer {}'.format(app.config['OAUTH_APP_TOKEN'])}
        url = app.config['BILLING_API'] + 'instruments/recurrent'
        return make_query('post', url, params, headers, 201)

    def send_sms_activation_code(self, msisdn, lang):
        """
        Calls the endpoint instruments/recurrent/send
        Source: https://api.icflix.com/doc/api/billing.html#method-instrument-validate-msisdn
        Returns the json parsed response or raise an HTTP error
        """
        params = {'msisdn': msisdn, 'lang': lang}
        headers = {'Authorization': 'Bearer {}'.format(app.config['OAUTH_APP_TOKEN'])}
        url = app.config['BILLING_API'] + 'instruments/recurrent/send'
        return make_query('post', url, params, headers, 201)

    def activate_msisdn(self, msisdn, activation_code, product_code, user_id, lang):
        """
        Calls the endpoint instruments/recurrent/activate
        Source: https://api.icflix.com/doc/api/billing.html#method-instrument-activate-msisdn
        Returns the json parsed response or raise an HTTP error
        """
        params = {
            'msisdn': msisdn,
            'activation_code': activation_code,
            'product_code': product_code,
            'user_id': user_id,
            'lang': lang
        }
        headers = {'Authorization': 'Bearer {}'.format(app.config['OAUTH_APP_TOKEN'])}
        url = app.config['BILLING_API'] + 'instruments/recurrent/activate'
        return make_query('post', url, params, headers, 201)
