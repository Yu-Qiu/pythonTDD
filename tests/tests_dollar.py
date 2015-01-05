__author__ = 'YuQiu'

import unittest
from dollar import Dollar


class TestDollar(unittest.TestCase):
    def test_multiplication(self):
        five = Dollar(5)
        ten = five * 2
        self.assertEquals(Dollar(10), ten)
        ten = five * 3
        self.assertEquals(Dollar(15), ten)

    def test_equality(self):
        self.assertEqual(Dollar(5), Dollar(5))
        self.assertNotEqual(Dollar(5), Dollar(6))