__author__ = 'YuQiu'


class Dollar:
    def __init__(self, amount):
        self.amount = amount

    def __mul__(self, multiplier):
        return Dollar(self.amount * multiplier)

    def __eq__(self, other):
        return self.amount == other.amount

    def __ne__(self, other):
        return not self == other