# Task ID: Mbpp/800

# Description/Response:
"""
Write a function to remove all whitespaces from a string.
assert remove_all_spaces('python  program')==('pythonprogram')
"""
def remove_all_spaces(string):
    return ''.join(string.split())