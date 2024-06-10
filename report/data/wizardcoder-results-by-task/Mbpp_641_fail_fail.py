# Task ID: Mbpp/641

# Description/Response:
"""
Write a function to find the nth nonagonal number.
assert is_nonagonal(10) == 325
"""
def is_nonagonal(n):
    return n * (n * n * (n * 2 - 1))