class Money(object):
    amount = 0

    def equals(self, money):
        return self.amount == money.amount

    def __eq__(self, money):
        return self.amount == money.amount


class Dollar(Money):

    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)


class Franc(Money):

    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        return Franc(self.amount * multiplier)
