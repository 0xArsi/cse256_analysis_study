# Task ID: Mbpp/165

# Description/Response:
"""
Write a function to count the number of characters in a string that occur at the same position in the string as in the English alphabet (case insensitive).
assert count_char_position("xbcefg") == 2
"""
def count_char_position(s):
    count = 0
    for i in range(len(s)):
        if s[i].lower() == chr(i + 97):
            count += 1
    return count