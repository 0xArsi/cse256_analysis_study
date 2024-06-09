# Task ID: Mbpp/437

# Description/Response:
"""
Write a function to remove odd characters in a string.
assert remove_odd("python")==("yhn")
"""
def remove_odd(string):
    return ''.join([char for i, char in enumerate(string) if i % 2 == 0])