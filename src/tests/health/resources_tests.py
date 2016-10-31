import unittest

import app


class HealthTests(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    def test_health_failure_401(self):
        rv = self.app.get('/health/')
        self.assertEqual(rv.status_code, 401)

    def test_health_failure_ok(self):
        rv = self.app.get('/health/?token={}'.format(app.app.config['APP_TOKEN']))
        self.assertEqual(rv.status_code, 200)
