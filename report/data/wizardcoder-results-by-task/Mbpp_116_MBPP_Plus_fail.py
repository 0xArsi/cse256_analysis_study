# Task ID: Mbpp/116

# Description/Response:
"""
Write a function to convert a given tuple of positive integers into a single integer.
assert tuple_to_int((1,2,3))==123
"""
def tuple_to_int(tup):
    result = 0
    for digit in tup:
        result = result * 10 + digit
    return result