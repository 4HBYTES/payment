import unittest

import mock

import auth.common.services.http as http
import mocks


class HttpTests(unittest.TestCase):
    def test_get_method_from_verb(self):
        method = http.get_method_from_verb('post')
        self.assertIsNotNone(method)

        method = http.get_method_from_verb('put')
        self.assertIsNotNone(method)

        method = http.get_method_from_verb('delete')
        self.assertIsNotNone(method)

        method = http.get_method_from_verb('patch')
        self.assertIsNotNone(method)

        method = http.get_method_from_verb('get')
        self.assertIsNotNone(method)

        method = http.get_method_from_verb(None)
        self.assertIsNotNone(method)

    @mock.patch(
        'auth.common.services.http.get_method_from_verb',
        side_effect=mocks.raise_connection_error
    )
    def test_make_query_raise_if_host_does_not_exist(self, mock_connection):
        with self.assertRaises(http.HttpError):
            http.make_query('get', 'http://localhost:1234')
            mock_connection.assert_called_with()

    @mock.patch(
        'auth.common.services.http.get_method_from_verb',
        side_effect=mocks.wrapped_status_code_500
    )
    def test_make_query_raise_if_status_code_not_ok(self, mock_status):
        with self.assertRaises(http.HttpError):
            http.make_query('get', 'http://localhost:1234')
            mock_status.assert_called_with()

    @mock.patch(
        'auth.common.services.http.get_method_from_verb',
        side_effect=mocks.wrapped_status_code_200
    )
    def test_make_query_raise_if_status_code_not_ok_manual(self, mock_status):
        with self.assertRaises(http.HttpError):
            http.make_query('delete', 'http://localhost:1234', {}, {}, 204)
            mock_status.assert_called_with()

    @mock.patch(
        'auth.common.services.http.get_method_from_verb',
        side_effect=mocks.wrapped_status_code_200
    )
    def test_make_query_status_code_ok(self, mock_status):
        response = http.make_query('get', 'http://localhost:1234')
        mock_status.assert_called_with('get')
        self.assertIsNotNone(response)
