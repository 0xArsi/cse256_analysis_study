# Task ID: Mbpp/137

# Description/Response:
"""
Write a function to find the ratio of zeroes to non-zeroes in an array of integers.
assert math.isclose(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, rel_tol=0.001)
"""
from math import isclose

def zero_count(arr):
    zero_count = 0
    non_zero_count = 0
    for num in arr:
        if num == 0:
            zero_count += 1
        else:
            non_zero_count += 1
    return zero_count / (zero_count + non_zero_count)