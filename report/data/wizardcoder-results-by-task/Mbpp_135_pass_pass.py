# Task ID: Mbpp/135

# Description/Response:
"""
Write a function to find the nth hexagonal number.
assert hexagonal_num(10) == 190
"""
def hexagonal_num(n):
    return n * (2*n - 1)