# Task ID: Mbpp/7

# Description/Response:
"""
Write a function to find all words which are at least 4 characters long in a string.
assert set(find_char_long('Please move back to stream')) == set(['Please', 'move', 'back', 'stream'])
"""
def find_char_long(string):
    return set(word for word in string.split() if len(word) >= 4)