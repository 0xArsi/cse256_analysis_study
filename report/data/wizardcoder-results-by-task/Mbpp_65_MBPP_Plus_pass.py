# Task ID: Mbpp/65

# Description/Response:
"""
Write a function to flatten a list and sum all of its elements.
assert recursive_list_sum(([1, 2, [3,4],[5,6]]))==21
"""
def recursive_list_sum(lst):
    total = 0
    for item in lst:
        if isinstance(item, list):
            total += recursive_list_sum(item)
        else:
            total += item
    return total