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
        return Money(amount, "USD")

    @staticmethod
    def franc(amount):
        return Money(amount, "CHF")

    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)

    def plus(self, addend):
        return Sum(self, addend)

    def reduce(self, bank, to):
        rate = bank.rate(self.currency, to)
        return Money(self.amount / rate, to)


class Bank(object):
    rates = {}

    def reduce(self, source, to):
        return source.reduce(self, to)

    def add_rate(self, _from, to, rate):
        self.rates.update({(_from, to): rate})

    def rate(self, _from, to):
        if _from == to:
            return 1
        return self.rates.get((_from, to))


class Expression(object):

    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def reduce(self, bank, to):
        raise NotImplementedError


class Sum(Expression):

    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend

    def reduce(self, bank, to):
        amount = self.augend.amount + self.addend.amount
        return Money(amount, to)
