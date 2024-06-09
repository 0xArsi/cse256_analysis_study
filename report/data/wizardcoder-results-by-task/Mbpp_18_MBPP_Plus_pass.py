# Task ID: Mbpp/18

# Description/Response:
"""
Write a function to remove characters from the first string which are present in the second string.
assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
"""
def remove_dirty_chars(s1, s2):
    for c in s2:
        s1 = s1.replace(c, '')
    return s1