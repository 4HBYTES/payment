from auth import app
from auth.common.services.http import make_query


class UserService(object):
    '''
    Service to wrap the access to the User API
    '''

    def get_current_profile(self, access_token):
        '''
        Calls the endpoint user/current
        Source: https://api.icflix.com/doc/api/user_profile.html#method-get-user-profile
        Returns the json parsed response or raise an HTTP error
        '''
        params = {}
        headers = {'Authorization': 'Bearer {}'.format(access_token)}
        url = app.config['USER_API'] + 'current'
        return make_query('get', url, params, headers)
