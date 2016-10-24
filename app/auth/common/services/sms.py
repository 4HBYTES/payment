from auth import app
from auth.common.services.http import make_query


class SmsService(object):
    """
    Service to wrap the access to the Sms Gateway API
    """

    def send(self, msisdn, partner, template, template_params):
        """
        Calls the endpoint sms/outgoing
        Source: https://api.icflix.com/doc/api/sms_gateway.html#method-send-outgoing-sms
        Returns the json parsed response or raise an HTTP error
        """
        params = {
            'destination': msisdn,
            'partner': partner,
            'template': template,
            'template_params': template_params
        }
        headers = {'Authorization': 'Bearer {}'.format(app.config['OAUTH_APP_TOKEN'])}
        url = app.config['SMS_API'] + 'outgoing'
        return make_query('get', url, params, headers, 201)

    def health(self):
        """
        Calls the endpoint sms/health
        Source: not documented
        Returns the json parsed response or raise an HTTP error
        """
        params = {}
        headers = {'Authorization': 'Bearer {}'.format(app.config['OAUTH_APP_TOKEN'])}
        url = app.config['SMS_API'] + 'health'
        return make_query('get', url, params, headers)
