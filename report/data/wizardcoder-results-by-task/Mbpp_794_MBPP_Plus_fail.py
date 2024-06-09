# Task ID: Mbpp/794

# Description/Response:
"""
Write a function that matches a string that has an 'a' followed by anything, ending in 'b'.
assert text_starta_endb("aabbbb")
"""
def text_starta_endb(s):
    return s.startswith('a') and s.endswith('b')