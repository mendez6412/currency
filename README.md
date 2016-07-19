# currency

# Currency Class
  Function:
  - Initiated with a currency type (USD, EUR, JPY, etc) and value (int/float)
  Methods:
  - __add__ : allows user to combine the two values of like-currency_type values
  - __sub__ : allows user to subtract second value from first value of like-currency_type values
  - __mul__ : allows user to multiply two like-currency_type values

# DifferentCurrencyCodeError Exception
  Function:
  - Provide an error code for an attempt to compute two different-currency_type values

#CurrencyConverter class
  Function:
  - Initiated with a dictionary of currency_types (key) and respective rates (value)
  Methods:
  - convert(): Takes a Currency class object and target, new currency_type and original to target

# UnknownCurrencyCodeError
  Function:
  - Provide an error code for an attempt to convert with an unknown currency_type
