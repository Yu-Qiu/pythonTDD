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