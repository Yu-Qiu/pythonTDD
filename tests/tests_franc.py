__author__ = 'YuQiu'

import unittest
from franc import Franc


class TestFranc(unittest.TestCase):
    def test_multiplication(self):
        five = Franc(5)
        ten = five * 2
        self.assertEquals(Franc(10), ten)
        ten = five * 3
        self.assertEquals(Franc(15), ten)

    def test_equality(self):
        self.assertEqual(Franc(5), Franc(5))
        self.assertNotEqual(Franc(5), Franc(6))