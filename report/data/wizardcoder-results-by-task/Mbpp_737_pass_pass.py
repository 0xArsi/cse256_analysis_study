# Task ID: Mbpp/737

# Description/Response:
"""
Write a function to check whether the given string is starting with a vowel or not using regex.
assert check_str("annie")
"""
import re

def check_str(string):
    vowels = re.compile(r'^[aeiouAEIOU]')
    if vowels.match(string):
        return True
    else:
        return False