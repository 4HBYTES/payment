import auth.common.services.http as http


class DummyResponse(object):
    def __init__(self, status_code):
        self.status_code = status_code

    def json(self):
        return {}


def make_query_200(verb, url, params, headers={}, status_code_ok=200):
        return DummyResponse(200)


def make_query_raise_error(verb, url, paranms, headers={}, status_code_ok=200):
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
