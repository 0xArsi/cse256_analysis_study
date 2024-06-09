# Task ID: Mbpp/58

# Description/Response:
"""
Write a python function to check whether the given two integers have opposite sign or not.
assert opposite_Signs(1,-2) == True
"""
def opposite_Signs(a, b):
    if a < 0 and b > 0 or a > 0 and b < 0:
        return True
    else:
        return False