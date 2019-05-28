import os
import unittest
from trails.helpers import singleton


class Sample(metaclass=singleton.Singleton):
    pass


class TestSingleton(unittest.TestCase):
    def test(self):
        instance = Sample()
        instance2 = Sample()
        self.assertTrue(id(instance)==id(instance2))


if __name__ == '__main__':
    unittest.main()
