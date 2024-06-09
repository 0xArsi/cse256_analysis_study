# Task ID: Mbpp/86

# Description/Response:
"""
Write a function to find nth centered hexagonal number.
assert centered_hexagonal_number(10) == 271
"""
def centered_hexagonal_number(n):
    return n * (n * 2 - 1)