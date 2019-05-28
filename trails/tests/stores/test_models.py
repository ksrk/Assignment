import unittest
from trails.stores import models


class TestModels(unittest.TestCase):
    def setUp(self):
        self._instance = models.Stores('stores.json')

    def test_get_stores_locations(self):
        ret = self._instance.get_stores_locations()
        self.assertIsInstance(ret, list)

    def test_stores(self):
        ret = self._instance.stores
        self.assertIsInstance(ret, list)


if __name__ == '__main__':
    unittest.main()
