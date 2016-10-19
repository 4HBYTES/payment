import unittest
import mock
from auth.common.services.products import ProductsService
import auth.common.services.http as http
import mocks


class OauthTests(unittest.TestCase):

    @mock.patch(
        'auth.common.services.products.make_query',
        side_effect=mocks.make_query_200
    )
    def test_get_payment_by_country_and_platform_ok(self, mock_status):
        service = ProductsService()
        response = service.get_payment_methods_by_country_and_platform('AE', 'website')
        mock_status.assert_called()
        self.assertIsNotNone(response)

    @mock.patch(
        'auth.common.services.products.make_query',
        side_effect=mocks.make_query_raise_error
    )
    def test_get_payment_by_country_and_platform_raise(self, mock_status):
        service = ProductsService()
        with self.assertRaises(http.HttpError):
            response = service.get_payment_methods_by_country_and_platform('AE', 'website')
            mock_status.assert_called()
            self.assertIsNone(response)

    @mock.patch(
        'auth.common.services.products.make_query',
        side_effect=mocks.make_query_200
    )
    def test_health_ok(self, mock_status):
        service = ProductsService()
        response = service.health()
        mock_status.assert_called()
        self.assertIsNotNone(response)

    @mock.patch(
        'auth.common.services.products.make_query',
        side_effect=mocks.make_query_raise_error
    )
    def test_health_raise(self, mock_status):
        service = ProductsService()
        with self.assertRaises(http.HttpError):
            response = service.health()
            mock_status.assert_called()
            self.assertIsNotNone(response)
