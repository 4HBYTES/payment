import auth.common.services.http as http


class DummyResponse(object):
    def __init__(self, status_code, extra={}):
        self.status_code = status_code
        self.extra = extra

    def json(self):
        return self.extra


def make_query_200(verb, url, params=None, headers={}, status_code_ok=200):
        return DummyResponse(200)


def make_query_raise_error(verb, url, params=None, headers={}, status_code_ok=200):
    raise http.HttpError('Nope')


def wrapped_status_code_500(verb):
    def method(url, params, headers):
        return DummyResponse(500)
    return method


def wrapped_status_code_200(verb):
    def method(url, params, headers):
        return DummyResponse(200)
    return method


def raise_connection_error(verb):
    def method(url, params, headers):
        raise http.ConnectionError('Nope')
    return method


class MockOauthService(object):
    '''
    Mocks the OauthService
    '''

    def get_by_email_ok(self, email):
        return DummyResponse(200)

    def get_by_email_failure(self, email):
        raise http.HttpError('Nope')

    def health_ok(self):
        return DummyResponse(200)

    def health_failure(self):
        raise http.HttpError('Nope')


class MockSmsService(object):
    '''
    Mocks the SmsService
    '''

    def health_ok(self):
        return DummyResponse(200)

    def health_failure(self):
        raise http.HttpError('Nope')


class MockUserService(object):
    '''
    Mocks the UserService
    '''

    def get_current_profile_none(self, access_token):
        raise http.HttpError('Nope')

    def get_current_profile_basic(self, access_token):
        return DummyResponse(200, {'subscription_status': 'free'}).json()

    def get_current_profile_premium(self, access_token):
        return DummyResponse(200, {'subscription_status': 'full'}).json()


class MockProductsService(object):
    '''
    Mocks the ProductService
    '''

    def health_ok(self):
        return DummyResponse(200)

    def health_failure(self):
        raise http.HttpError('Nope')
