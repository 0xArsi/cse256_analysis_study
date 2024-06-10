# Task ID: Mbpp/566

# Description/Response:
"""
Write a function to get the sum of the digits of a non-negative integer.
assert sum_digits(345)==12
"""
def sum_digits(n):
    """
    Returns the sum of the digits of a non-negative integer.
    """
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total