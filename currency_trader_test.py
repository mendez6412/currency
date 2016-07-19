from nose.tools import assert_raises
from currency import Currency, DifferentCurrencyCodeError
from currency_converter import CurrencyConverter, UnknownCurrencyCodeError
from currency_trader import CurrencyTrader

def test_CurrencyTrader():
    rates1 = CurrencyConverter({'USD': 1, 'EUR': .9, 'JPY': 106, 'GBP': .76})
    rates2 = CurrencyConverter({'USD': 1, 'EUR': .8, 'JPY': 120, 'GBP': .60})
    value = Currency('EUR', 1000)

    test = CurrencyTrader(rates1, rates2, value)

    assert test.first_rates == rates1
    assert test.second_rates == rates2
    assert test.value == value

def test_get_first_and_second_rates():
    rates1 = CurrencyConverter({'USD': 1, 'EUR': .9, 'JPY': 106, 'GBP': .76})
    rates2 = CurrencyConverter({'USD': 1, 'EUR': .8, 'JPY': 120, 'GBP': .60})
    value = Currency('EUR', 1000)

    test = CurrencyTrader(rates1, rates2, value)
    result = {'USD': 1000/.9, 'EUR': 1000, 'JPY': (1000 * 106)/.9, 'GBP': (1000 * .76)/.9}

    result2 = {'USD': 1000/.8, 'EUR': 1000, 'JPY': (1000 * 120)/.8, 'GBP': (1000 * .60)/.8}


    assert test.get_first_values() == result
    assert test.get_second_values() == result2

def test_get_differences():
    rates1 = CurrencyConverter({'USD': 1, 'EUR': .9, 'JPY': 106, 'GBP': .76})
    rates2 = CurrencyConverter({'USD': 1, 'EUR': .8, 'JPY': 120, 'GBP': .60})
    value = Currency('EUR', 1000)

    test = CurrencyTrader(rates1, rates2, value)
    result = {'USD': ((1000/.8)- (1000/.9)), 'EUR': (1000 - 1000), 'JPY': ((1000 * 120)/.8) - ((1000 * 106)/.9), 'GBP': ((1000 * .60)/.8) - (1000 * .76/.9)}
    assert test.get_differences() == result

def test_get_max_difference():
    rates1 = CurrencyConverter({'USD': 1, 'EUR': .9, 'JPY': 106, 'GBP': .76})
    rates2 = CurrencyConverter({'USD': 1, 'EUR': .8, 'JPY': 120, 'GBP': .60})
    value = Currency('EUR', 1000)

    test = CurrencyTrader(rates1, rates2, value)
    result = 'JPY'

    assert test.get_max_difference() == result
