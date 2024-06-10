# Task ID: Mbpp/222

# Description/Response:
"""
Write a function to check if all the elements in tuple have same data type or not.
assert check_type((5, 6, 7, 3, 5, 6) ) == True
"""
def check_type(tup):
    return len(set(type(i) for i in tup)) == 1