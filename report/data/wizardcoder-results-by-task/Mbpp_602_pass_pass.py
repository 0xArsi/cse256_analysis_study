# Task ID: Mbpp/602

# Description/Response:
"""
Write a python function to find the first repeated character in a given string.
assert first_repeated_char("abcabc") == "a"
"""
def first_repeated_char(s):
    seen = set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return None