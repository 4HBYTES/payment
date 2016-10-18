import unittest
import mock
from auth.common.services.user import UserService
import auth.common.services.http as http
import mocks


class UserTests(unittest.TestCase):

    @mock.patch(
        'auth.common.services.user.make_query',
        side_effect=mocks.make_query_200
    )
    def test_get_current_profile_ok(self, mock_status):
        service = UserService()
        response = service.get_current_profile('random-access-token')
        mock_status.assert_called()
        self.assertIsNotNone(response)

    @mock.patch(
        'auth.common.services.user.make_query',
        side_effect=mocks.make_query_raise_error
    )
    def test_get_current_profile_raise(self, mock_raise):
        service = UserService()
        with self.assertRaises(http.HttpError):
            response = service.get_current_profile('random-access-token')
            mock_raise.assert_called()
            self.assertIsNone(response)
