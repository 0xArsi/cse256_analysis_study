# Task ID: Mbpp/59

# Description/Response:
"""
Write a function to find the nth octagonal number.
assert is_octagonal(5) == 65
"""
def is_octagonal(n):
    return n**2 + n*(n-1)