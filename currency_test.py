from nose.tools import assert_raises
from currency import Currency, DifferentCurrencyCodeError

def test_Currency():
    one_usd = Currency('USD', 1)
    two_eur = Currency('EUR', 2)

    test1 = one_usd
    test2 = two_eur

    assert test1.currency_type == 'USD'
    assert test2.currency_type == 'EUR'
    assert test1.value == 1
    assert test2.value == 2

def test_is_two_of_same_currency():
    amount1 = Currency('USD', 3)
    amount2 = Currency('USD', 3)

    assert amount1 == amount2

def test_is_not_two_of_same_currency():
    amount1 = Currency('USD', 1)
    amount2 = Currency('EUR', 1)

    assert amount1 != amount2

def test_add():
    amount1 = Currency('USD', 1)
    amount2 = Currency('USD', 2)

    result = amount1 + amount2

    assert result.currency_type == 'USD'
    assert result.value == 3

def test_sub():
    amount1 = Currency('EUR', 3)
    amount2 = Currency('EUR', 2)

    result = amount1 - amount2

    assert result.currency_type == 'EUR'
    assert result.value == 1

def test_is_error():
    amount1 = Currency('USD', 3)
    amount2 = Currency('EUR', 4)

    assert_raises(DifferentCurrencyCodeError, Currency.__add__, amount1, amount2)
