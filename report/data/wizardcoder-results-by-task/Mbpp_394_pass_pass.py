# Task ID: Mbpp/394

# Description/Response:
"""
Write a function to check if given tuple contains no duplicates.
assert check_distinct((1, 4, 5, 6, 1, 4)) == False
"""
def check_distinct(tup):
    return len(tup) == len(set(tup))