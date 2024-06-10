# Task ID: Mbpp/91

# Description/Response:
"""
Write a function to check if a string is present as a substring in a given list of string values.
assert find_substring(["red", "black", "white", "green", "orange"],"ack")==True
"""
def find_substring(lst, sub):
    for s in lst:
        if sub in s:
            return True
    return False