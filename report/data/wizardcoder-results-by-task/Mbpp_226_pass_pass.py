# Task ID: Mbpp/226

# Description/Response:
"""
Write a python function to remove the characters which have odd index values of a given string.
assert odd_values_string('abcdef') == 'ace'
"""
def odd_values_string(string):
    return ''.join([char for i, char in enumerate(string) if i % 2 == 0])