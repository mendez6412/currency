from nose.tools import assert_raises
from currency_converter import CurrencyConverter, UnknownCurrencyCodeError
from currency import Currency, DifferentCurrencyCodeError

def test_CurrencyConverter():
    rate_chart = CurrencyConverter({'USD': 1.0, 'EUR': .9, 'JPY': 106.18 })

    assert rate_chart.rates == {'USD': 1.0, 'EUR': .9, 'JPY': 106.18 }

def test_convert():
    rate_chart = CurrencyConverter({'USD': 1.0, 'EUR': .9, 'JPY': 106.18 })

    amount1 = Currency('USD', 2)
    converted1 = rate_chart.convert(amount1, 'USD')

    amount2 = Currency('EUR', 1)
    converted2 = rate_chart.convert(amount2, 'EUR')

    amount3 = (2 * .9) # $2 to Euros
    converted3 = rate_chart.convert(Currency('USD', 2), 'EUR')

    amount4 = (400 * .0084) # ¥400 to Euros
    converted4 = rate_chart.convert(Currency('JPY', 400), 'EUR')

    assert converted1 == amount1
    assert converted2 == amount2
    assert converted3.value == amount3

def test_is_error():
    rate_chart = CurrencyConverter({'USD': 1.0, 'EUR': .9, 'JPY': 106.18 })

    amount = Currency('GBP', 10)

    assert_raises(UnknownCurrencyCodeError, rate_chart.convert, amount, 'EUR')
