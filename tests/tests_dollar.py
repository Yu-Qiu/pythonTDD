__author__ = 'YuQiu'

import unittest
from dollar import Dollar

class TestDollar(unittest.TestCase):

    def test_multiplication(self):
        five = Dollar(5)
        ten = five * 2
        self.assertEquals(10, ten.amount)
        ten = five * 3
        self.assertEquals(15, ten.amount)

    def test_equality(self):
        self.assertEqual(Dollar(5), Dollar(5))
        self.assertNotEqual(Dollar(5), Dollar(6))