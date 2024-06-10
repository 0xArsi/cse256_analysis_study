# Task ID: Mbpp/797

# Description/Response:
"""
Write a python function to find the sum of all odd natural numbers within the range l and r.
assert sum_in_range(2,5) == 8
"""
def sum_in_range(l, r):
    """
    Returns the sum of all odd natural numbers within the range l and r (inclusive).
    """
    return sum(range(l, r+1, 2))