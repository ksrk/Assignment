import unittest
from trails import app


class TestModels(unittest.TestCase):
    def setUp(self):
        self._app = app.create_app()
        self._client = self._app.test_client()

    def test_get_stores(self):
        ret = self._client.get('/stores')
        self.assertTrue(ret.status_code in [200, 404])

    def test_get_stores_radius(self):
        ret = self._client.get('/stores/AL95JP/5')
        self.assertTrue(ret.status_code in [200, 404])


if __name__ == '__main__':
    unittest.main()
