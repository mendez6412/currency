from currency import Currency, DifferentCurrencyCodeError

class CurrencyConverter():
    def __init__(self, rates):
        self.rates = rates

    def convert(self, value, code):
        if code == value.currency_type:
            return value
        if code not in self.rates or value.currency_type not in self.rates:
            raise UnknownCurrencyCodeError
        total = (value.value * self.rates[code])/self.rates[value.currency_type]
        return Currency(value.currency_type, total)

class UnknownCurrencyCodeError(Exception):
    pass
