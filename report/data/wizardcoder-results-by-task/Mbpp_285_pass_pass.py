# Task ID: Mbpp/285

# Description/Response:
"""
Write a function that checks whether a string contains the 'a' character followed by two or three 'b' characters.
assert text_match_two_three("ac")==(False)
"""
def text_match_two_three(string):
    if 'a' in string and string.count('b') >= 2:
        return True
    else:
        return False