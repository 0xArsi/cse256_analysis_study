# Task ID: Mbpp/294

# Description/Response:
"""
Write a function to find the maximum value in a given heterogeneous list.
assert max_val(['Python', 3, 2, 4, 5, 'version'])==5
"""
def max_val(lst):
    max_val = lst[0]
    for val in lst:
        if val > max_val:
            max_val = val
    return max_val