import unittest
import mock
from auth.common.services.billing import BillingService
import auth.common.services.http as http
import mocks


class BillingTests(unittest.TestCase):

    @mock.patch(
        'auth.common.services.billing.make_query',
        side_effect=mocks.make_query_200
    )
    def test_create_sms_instrument_ok(self, mock_status):
        service = BillingService()
        response = service.create_sms_instrument('971154324565', 'duae', 'random')
        mock_status.assert_called()
        self.assertIsNotNone(response)

    @mock.patch(
        'auth.common.services.billing.make_query',
        side_effect=mocks.make_query_raise_error
    )
    def test_create_sms_instrument_raise(self, mock_raise):
        service = BillingService()
        with self.assertRaises(http.HttpError):
            response = service.create_sms_instrument('971154324565', 'duae', 'random')
            mock_raise.assert_called()
            self.assertIsNone(response)

    @mock.patch(
        'auth.common.services.billing.make_query',
        side_effect=mocks.make_query_200
    )
    def test_send_sms_activation_code_ok(self, mock_status):
        service = BillingService()
        response = service.send_sms_activation_code('971154324565', 'fra')
        mock_status.assert_called()
        self.assertIsNotNone(response)

    @mock.patch(
        'auth.common.services.billing.make_query',
        side_effect=mocks.make_query_raise_error
    )
    def test_send_sms_activation_code_raise(self, mock_raise):
        service = BillingService()
        with self.assertRaises(http.HttpError):
            response = service.send_sms_activation_code('971154324565', 'fra')
            mock_raise.assert_called()
            self.assertIsNone(response)

    @mock.patch(
        'auth.common.services.billing.make_query',
        side_effect=mocks.make_query_200
    )
    def test_activate_msisdn_ok(self, mock_status):
        service = BillingService()
        response = service.activate_msisdn('971154324565', '123456', 'random', 'user-uuid', 'fra')
        mock_status.assert_called()
        self.assertIsNotNone(response)

    @mock.patch(
        'auth.common.services.billing.make_query',
        side_effect=mocks.make_query_raise_error
    )
    def test_activate_msisdn_raise(self, mock_raise):
        service = BillingService()
        with self.assertRaises(http.HttpError):
            response = service.activate_msisdn('971154324565', '123456', 'random', 'user-uuid', 'fra')
            mock_raise.assert_called()
            self.assertIsNone(response)
