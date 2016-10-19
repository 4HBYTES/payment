from auth import app
from auth.common.services.http import make_query


class OauthService(object):
    '''
    Service to wrap the access to the Oauth API
    '''

    def get_by_email(self, email):
        '''
        Calls the endpoint oauth/user/byemail
        Source: https://api.icflix.com/doc/api/authentication.html#method-get-https-secureicflixcomio-v-api_version-platform-oauth-user-byemail
        Returns the json parsed response or raise an HTTP error
        '''
        params = {'email': email}
        headers = {'Authorization': 'Bearer {}'.format(app.config['OAUTH_APP_TOKEN'])}
        url = app.config['OAUTH_API'] + 'user/byemail'
        return make_query('get', url, params, headers)

    def health(self):
        '''
        Calls the endpoint oauth/health
        Source: not documented
        Returns the json parsed response or raise an HTTP error
        '''
        params = {}
        url = app.config['OAUTH_API'] + 'health'
        return make_query('get', url, params)
