class Currency():
    def __init__(self, currency_type, value):
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

class DifferentCurrencyCodeError(Exception):
    pass
