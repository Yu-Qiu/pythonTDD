__author__ = 'YuQiu'

import unittest
from dollar import Dollar

class TestDollar(unittest.TestCase):

    def test_multiplication(self):
        five = Dollar(5)
        five.times(2)
        self.assertEquals(10, five.amount)