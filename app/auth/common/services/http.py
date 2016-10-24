"""
Collection of utilities to wrap the HTTP client used in this app.
This should be used instead of the HTTP client directly, so that
it can be changed transparently and logic can be wrapped, such
as the logging of errors.
"""

import requests


class HttpError(requests.HTTPError):
    pass


class ConnectionError(requests.ConnectionError):
    pass


def get_method_from_verb(verb):
    """
    Returns the appropriate requests method based on
    the http verb given in parameter.
    """
    if verb == 'post':
        return requests.post
    elif verb == 'put':
        return requests.put
    elif verb == 'delete':
        return requests.delete
    elif verb == 'patch':
        return requests.patch
    else:
        return requests.get


def make_query(verb, url, params=None, headers={}, status_code_ok=200):
    """
    Calls the given url with all the parameters. An HTTP error is raised
    if the response's status code is different than status_code_ok.
    In case of success, returns the response in json format.
    """
    method = get_method_from_verb(verb)

    try:
        response = method(url, params=params, headers=headers)
    except ConnectionError:
        message = 'Nested HTTP Error : Failed to establish a connection - {}'.format(url)
        raise HttpError(message)

    if response.status_code != status_code_ok:
        message = 'Nested HTTP Error : {} - {}'.format(response.status_code, url)
        raise HttpError(message)

    return response.json()
