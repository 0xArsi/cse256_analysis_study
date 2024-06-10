# Task ID: Mbpp/126

# Description/Response:
"""
Write a python function to find the sum of common divisors of two given numbers.
assert sum(10,15) == 6
"""
def sum_common_divisors(a, b):
    """
    Returns the sum of common divisors of two given numbers.
    """
    divisors = set(range(1, min(a, b) + 1))
    return sum(d for d in divisors if a % d == 0 and b % d == 0)