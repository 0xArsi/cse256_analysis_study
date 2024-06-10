# Task ID: Mbpp/478

# Description/Response:
"""
Write a function to remove lowercase substrings from a given string.
assert remove_lowercase("PYTHon")==('PYTH')
"""
def remove_lowercase(s):
    return ''.join(c for c in s if c.isupper() or c.isdigit())