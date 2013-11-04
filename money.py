class Money(object):

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def equals(self, money):
        return self.__eq__(money)

    def __eq__(self, money):
        return self.amount == money.amount and self.currency == money.currency

    @staticmethod
    def dollar(amount):
        return Dollar(amount, "USD")

    @staticmethod
    def franc(amount):
        return Franc(amount, "CHF")

    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)


class Dollar(Money):
    pass


class Franc(Money):
    pass
