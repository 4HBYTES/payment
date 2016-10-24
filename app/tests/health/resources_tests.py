import unittest

import mock

import auth
from tests.common.services.mocks import MockOauthService, MockSmsService, \
    MockProductsService

mock_oauth_service = MockOauthService()
mock_sms_service = MockSmsService()
mock_products_service = MockProductsService()


class HealthTests(unittest.TestCase):
    def setUp(self):
        self.app = auth.app.test_client()

    def test_health_failure_401(self):
        rv = self.app.get('/health/')
        self.assertEqual(rv.status_code, 401)

    @mock.patch(
        'auth.health.resources.HealthDetails.oauth_service.health',
        side_effect=mock_oauth_service.health_failure
    )
    def test_health_failure_oauth_down(self, mock_oauth_service):
        rv = self.app.get('/health/?token={}'.format(auth.app.config['APP_TOKEN']))
        self.assertEqual(rv.status_code, 500)
        mock_oauth_service.assert_called()

    @mock.patch(
        'auth.health.resources.HealthDetails.oauth_service.health',
        side_effect=mock_oauth_service.health_ok
    )
    @mock.patch(
        'auth.health.resources.HealthDetails.sms_service.health',
        side_effect=mock_sms_service.health_failure
    )
    def test_health_failure_sms_down(self, mock_sms_service, mock_oauth_service):
        rv = self.app.get('/health/?token={}'.format(auth.app.config['APP_TOKEN']))
        self.assertEqual(rv.status_code, 500)
        mock_sms_service.assert_called()
        mock_oauth_service.assert_called()

    @mock.patch(
        'auth.health.resources.HealthDetails.oauth_service.health',
        side_effect=mock_oauth_service.health_ok
    )
    @mock.patch(
        'auth.health.resources.HealthDetails.sms_service.health',
        side_effect=mock_sms_service.health_ok
    )
    @mock.patch(
        'auth.health.resources.HealthDetails.products_service.health',
        side_effect=mock_products_service.health_failure
    )
    def test_health_failure_products_down(self, mock_products_service, mock_sms_service, mock_oauth_service):
        rv = self.app.get('/health/?token={}'.format(auth.app.config['APP_TOKEN']))
        self.assertEqual(rv.status_code, 500)
        mock_products_service.assert_called()
        mock_sms_service.assert_called()
        mock_oauth_service.assert_called()

    @mock.patch(
        'auth.health.resources.HealthDetails.products_service.health',
        side_effect=mock_products_service.health_ok
    )
    @mock.patch(
        'auth.health.resources.HealthDetails.oauth_service.health',
        side_effect=mock_oauth_service.health_ok
    )
    @mock.patch(
        'auth.health.resources.HealthDetails.sms_service.health',
        side_effect=mock_sms_service.health_ok
    )
    def test_health_ok(self, mock_sms_service, mock_oauth_service, mock_products_service):
        rv = self.app.get('/health/?token={}'.format(auth.app.config['APP_TOKEN']))
        self.assertEqual(rv.status_code, 200)
        mock_sms_service.assert_called()
        mock_oauth_service.assert_called()
        mock_products_service.assert_called()
