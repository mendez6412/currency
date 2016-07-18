class Currency():
    def __init__(self, currency_type, value = None):
        if value == None:
            sign = currency_type[0]
            value = float(currency_type[1:])
            if sign == '$':
                currency_type = 'USD'
            if sign == '€':
                currency_type = 'EUR'
            if sign == '£':
                currency_type = 'GBP'
            if sign == '¥':
                currency_type = 'JPY'
        self.currency_type = currency_type
        self.value = value

    def __eq__(self, other):
        return self.value == other.value and self.currency_type == other.currency_type

    def __add__(self, other):
        try:
            if self.currency_type != other.currency_type:
                raise DifferentCurrencyCodeError
            return Currency(self.currency_type, self.value + other.value)
        except ValueError:
            pass

    def __sub__(self, other):
        return Currency(self.currency_type, self.value - other.value)

    def __mul__(self, other):
        return Currency(self.currency_type, self.value * other)

class DifferentCurrencyCodeError(Exception):
    pass
