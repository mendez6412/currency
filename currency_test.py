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

def test_mul():
    amount1 = Currency('EUR', 4)

    result = amount1 * 3
    result2 = amount1 * 3.0

    assert result.value == 12
    assert result2.value == 12.0

def test_ony_one_variable():
    amount1 = Currency('$300')
    amount2 = Currency('€20.50')

    assert amount1.currency_type == 'USD'
    assert amount1.value == 300
    assert amount2.currency_type == 'EUR'
    assert amount2.value == 20.50
