class Money(object):
    amount = 0
    currency = ''

    def equals(self, money):
        return self.amount == money.amount and self.__class__ == money.__class__

    def __eq__(self, money):
        return self.amount == money.amount

    @staticmethod
    def dollar(amount):
        return Dollar(amount, "USD")

    @staticmethod
    def franc(amount):
        return Franc(amount, "CHF")


class Dollar(Money):

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def times(self, multiplier):
        return Money.dollar(self.amount * multiplier)


class Franc(Money):

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def times(self, multiplier):
        return Money.franc(self.amount * multiplier)
