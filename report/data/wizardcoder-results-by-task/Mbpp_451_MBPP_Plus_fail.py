# Task ID: Mbpp/451

# Description/Response:
"""
Write a function to remove all whitespaces from the given string.
assert remove_whitespaces(' Google    Flutter ') == 'GoogleFlutter'
"""
def remove_whitespaces(string):
    return ''.join(string.split())