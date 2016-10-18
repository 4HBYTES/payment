import unittest
import mock
from auth.common.services.sms import SmsService
import auth.common.services.http as http
import mocks


class SmsTests(unittest.TestCase):

    @mock.patch(
        'auth.common.services.sms.make_query',
        side_effect=mocks.make_query_200
    )
    def test_get_current_profile_ok(self, mock_status):
        service = SmsService()
        response = service.send('971651234561', 'duae', 'express_welcome', {})
        mock_status.assert_called()
        self.assertIsNotNone(response)

    @mock.patch(
        'auth.common.services.sms.make_query',
        side_effect=mocks.make_query_raise_error
    )
    def test_get_current_profile_raise(self, mock_raise):
        service = SmsService()
        with self.assertRaises(http.HttpError):
            response = service.send('971651234561', 'duae', 'express_welcome', {})
            mock_raise.assert_called()
            self.assertIsNone(response)
