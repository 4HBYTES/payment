import auth.common.services.http as http


class DummyResponse(object):
    def __init__(self, status_code):
        self.status_code = status_code

    def json(self):
        return {}


def make_query_200(verb, url, params, headers):
        return DummyResponse(200)


def make_query_raise_error(verb, url, paranms, headers):
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
