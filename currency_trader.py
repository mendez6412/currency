from currency_converter import CurrencyConverter, UnknownCurrencyCodeError
from currency import Currency, DifferentCurrencyCodeError
import operator

class CurrencyTrader(CurrencyConverter):
    def __init__(self, first_rates, second_rates, value):
        self.first_rates = first_rates
        self.second_rates = second_rates
        self.value = value


    def get_first_values(self):
        d = {}
        for item in self.first_rates.rates.keys():
            d[item] = (self.first_rates.convert(self.value, item)).value
        return d

    def get_second_values(self):
        d = {}
        for item in self.second_rates.rates.keys():
            d[item] = (self.second_rates.convert(self.value, item)).value
        return d

    def get_differences(self):
        time1 = self.get_first_values()
        time2 = self.get_second_values()
        difference = {}
        for item in time1:
            difference[item] = time2[item] - time1[item]
        print(difference)
        return difference

    def get_max_difference(self):
        difference_dictionary = self.get_differences()
        max_dictionary = {}
        for item in difference_dictionary:
            max_dictionary[item] = self.second_rates.convert(Currency(item, difference_dictionary[item]), self.value.currency_type).value
        max_dif = max(max_dictionary.keys(), key=(lambda key: max_dictionary[key]))
        print(max_dictionary)
        return max_dif
