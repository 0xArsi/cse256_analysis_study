# Task ID: Mbpp/591

# Description/Response:
"""
Write a python function to interchange the first and last elements in a list.
assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]
"""
def swap_List(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst