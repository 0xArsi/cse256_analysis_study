# Task ID: Mbpp/773

# Description/Response:
"""
Write a function to find the occurrence and position of the substrings within a string. Return None if there is no match.
assert occurance_substring('python programming, python language','python')==('python', 0, 6)
"""
def occurance_substring(string, substring):
    if substring in string:
        return (substring, string.index(substring), string.index(substring) + len(substring) - 1)
    else:
        return None