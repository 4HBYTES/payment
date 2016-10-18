import unittest
import mock
from auth.common.services.oauth import OauthService
import auth.common.services.http as http
import mocks


class OauthTests(unittest.TestCase):

    @mock.patch(
        'auth.common.services.oauth.make_query',
        side_effect=mocks.make_query_200
    )
    def test_get_by_email_ok(self, mock_status):
        service = OauthService()
        response = service.get_by_email('test-auth-v3@icflix.com')
        mock_status.assert_called()
        self.assertIsNotNone(response)

    @mock.patch(
        'auth.common.services.oauth.make_query',
        side_effect=mocks.make_query_raise_error
    )
    def test_get_by_email_raise(self, mock_raise):
        service = OauthService()
        with self.assertRaises(http.HttpError):
            response = service.get_by_email('test-auth-v3@icflix.com')
            mock_raise.assert_called()
            self.assertIsNone(response)

    @mock.patch(
        'auth.common.services.oauth.make_query',
        side_effect=mocks.make_query_200
    )
    def test_health_ok(self, mock_status):
        service = OauthService()
        response = service.health()
        mock_status.assert_called()
        self.assertIsNotNone(response)

    @mock.patch(
        'auth.common.services.oauth.make_query',
        side_effect=mocks.make_query_raise_error
    )
    def test_health_raise(self, mock_raise):
        service = OauthService()
        with self.assertRaises(http.HttpError):
            response = service.health()
            mock_raise.assert_called()
            self.assertIsNone(response)
