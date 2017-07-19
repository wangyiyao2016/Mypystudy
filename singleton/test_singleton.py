

import unittest
from singleton import Singleton


@Singleton
class A(object):
    pass


class TestSingleton(unittest.TestCase):
    def testSingleton(self):
        a = A.Instance()
        aa = A.Instance()
        self.assertTrue(a is aa)

    def testSingletonCall(self):
        a = A()
        aa = A()
        self.assertTrue(a is aa)

    def testIsinstance(self):
        a = A.Instance()
        self.assertTrue(isinstance(a, A))
        self.assertFalse(isinstance(a, list))


if __name__ == "__main__":
    unittest.main()
