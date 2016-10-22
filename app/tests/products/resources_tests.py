import unittest
import mock
import json

from tests.common.services.mocks import MockProductsService

import auth

mock_products_service = MockProductsService()


class ProductsTests(unittest.TestCase):

    def setUp(self):
        self.app = auth.app.test_client()

    @mock.patch(
        'auth.products.resources.ProductsResource.products_service.get_payment_methods_by_country_and_platform',
        side_effect=mock_products_service.get_payment_methods_raise
    )
    def test_products_down(self, mock_products):
        rv = self.app.get('/products/duae')
        self.assertEqual(rv.status_code, 503)

        mock_products.assert_called()

    @mock.patch(
        'auth.products.resources.ProductsResource.products_service.get_payment_methods_by_country_and_platform',
        side_effect=mock_products_service.get_payment_methods_no_telcos
    )
    def test_products_no_telcos(self, mock_products):
        rv = self.app.get('/products/duae')
        self.assertEqual(rv.status_code, 404)

        mock_products.assert_called()

    @mock.patch(
        'auth.products.resources.ProductsResource.products_service.get_payment_methods_by_country_and_platform',
        side_effect=mock_products_service.get_payment_methods_no_sms_recurrent
    )
    def test_products_no_sms_recurrent(self, mock_products):
        rv = self.app.get('/products/duae')
        self.assertEqual(rv.status_code, 404)

        mock_products.assert_called()

    @mock.patch(
        'auth.products.resources.ProductsResource.products_service.get_payment_methods_by_country_and_platform',
        side_effect=mock_products_service.get_payment_methods_no_client_meta
    )
    def test_products_no_client_meta(self, mock_products):
        rv = self.app.get('/products/duae')
        self.assertEqual(rv.status_code, 404)

        mock_products.assert_called()

    @mock.patch(
        'auth.products.resources.ProductsResource.products_service.get_payment_methods_by_country_and_platform',
        side_effect=mock_products_service.get_payment_methods_client_meta_empty
    )
    def test_products_client_meta_empty(self, mock_products):
        rv = self.app.get('/products/duae')
        self.assertEqual(rv.status_code, 404)

        mock_products.assert_called()

    @mock.patch(
        'auth.products.resources.ProductsResource.products_service.get_payment_methods_by_country_and_platform',
        side_effect=mock_products_service.get_payment_methods_client_meta_false
    )
    def test_products_client_meta_false(self, mock_products):
        rv = self.app.get('/products/duae')
        self.assertEqual(rv.status_code, 404)

        mock_products.assert_called()

    @mock.patch(
        'auth.products.resources.ProductsResource.products_service.get_payment_methods_by_country_and_platform',
        side_effect=mock_products_service.get_payment_methods_ok
    )
    def test_products_ok(self, mock_products):
        rv = self.app.get('/products/duae')
        self.assertEqual(rv.status_code, 200)

        mock_products.assert_called()

    @mock.patch(
        'auth.products.resources.ProductsResource.products_service.get_payment_methods_by_country_and_platform',
        side_effect=mock_products_service.get_payment_methods_ok
    )
    def test_products_product_uuid_ok(self, mock_products):
        dummy_uuid = '1234-1234-4321-4321'
        rv = self.app.get('/products/duae/{}'.format(dummy_uuid))
        self.assertEqual(rv.status_code, 200)

        json_data = json.loads(rv.data)
        self.assertEqual(json_data['products'][0]['uuid'], dummy_uuid)
        mock_products.assert_called()

    @mock.patch(
        'auth.products.resources.ProductsResource.products_service.get_payment_methods_by_country_and_platform',
        side_effect=mock_products_service.get_payment_methods_ok
    )
    def test_products_product_uuid_not_ok(self, mock_products):
        dummy_uuid = '1234-1234'
        rv = self.app.get('/products/duae/{}'.format(dummy_uuid))
        self.assertEqual(rv.status_code, 200)

        json_data = json.loads(rv.data)
        self.assertNotEqual(json_data['products'][0]['uuid'], dummy_uuid)
        mock_products.assert_called()
