# Task ID: Mbpp/787

# Description/Response:
"""
Write a function that matches a string that has an a followed by three 'b'.
assert not text_match_three("ac")
"""
def text_match_three(text):
    if text[0] == 'a' and text[1:4] == 'bbb':
        return True
    else:
        return False