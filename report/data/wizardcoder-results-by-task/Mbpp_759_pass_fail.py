# Task ID: Mbpp/759

# Description/Response:
"""
Write a function to check whether a given string is a decimal number with a precision of 2.
assert is_decimal('123.11')==True
"""
def is_decimal(s):
    try:
        float_num = float(s)
        if float_num.is_integer():
            return False
        else:
            return round(float_num, 2) == float_num
    except ValueError:
        return False