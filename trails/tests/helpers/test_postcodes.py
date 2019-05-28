import unittest
from trails.helpers import postcodes


class TestPostcodes(unittest.TestCase):
    def setUp(self):
        self._url = postcodes.url.format('GU50BD')

    def test_get_details(self):
        ret = postcodes.get_details(self._url)
        self.assertIsInstance(ret, dict)

    def test_find_the_distance(self):
        destination = {"longitude": -0.499536, "latitude": 51.431688}
        source = {"longitude": -0.277158, "latitude": 51.386159}
        ret = postcodes.find_the_distance(source, destination)
        self.assertTrue(ret)


if __name__ == '__main__':
    unittest.main()
