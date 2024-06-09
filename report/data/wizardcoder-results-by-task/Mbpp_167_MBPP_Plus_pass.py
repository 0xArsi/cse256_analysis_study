# Task ID: Mbpp/167

# Description/Response:
"""
Write a python function to find the smallest power of 2 greater than or equal to n.
assert next_power_of_2(0) == 1
"""
def next_power_of_2(n):
    """
    Returns the smallest power of 2 greater than or equal to n.
    """
    return 1 if n == 0 else 2**(n-1).bit_length()