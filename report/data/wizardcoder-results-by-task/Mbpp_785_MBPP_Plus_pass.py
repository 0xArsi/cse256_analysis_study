# Task ID: Mbpp/785

# Description/Response:
"""
Write a function to convert tuple string to integer tuple.
assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
"""
def tuple_str_int(tup_str):
    return tuple(map(int, tup_str.strip('()').split(',')))