# Task ID: Mbpp/16

# Description/Response:
"""
Write a function to that returns true if the input string contains sequences of lowercase letters joined with an underscore and false otherwise.
assert text_lowercase_underscore("aab_cbbbc")==(True)
"""
def text_lowercase_underscore(s):
    """
    Returns True if the input string contains sequences of lowercase letters joined with an underscore, False otherwise.
    """
    for i in range(len(s)-1):
        if s[i] == '_':
            if not s[i+1].islower():
                return False
    return s.islower()