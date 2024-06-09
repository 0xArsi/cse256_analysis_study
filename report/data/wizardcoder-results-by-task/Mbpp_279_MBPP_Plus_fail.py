# Task ID: Mbpp/279

# Description/Response:
"""
Write a function to find the nth decagonal number.
assert is_num_decagonal(3) == 27
"""
def is_num_decagonal(n):
    return n * ((n * (n - 1)) // 2)