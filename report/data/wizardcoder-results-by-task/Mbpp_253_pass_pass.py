# Task ID: Mbpp/253

# Description/Response:
"""
Write a python function that returns the number of integer elements in a given list.
assert count_integer([1,2,'abc',1.2]) == 2
"""
def count_integer(lst):
    count = 0
    for element in lst:
        if isinstance(element, int):
            count += 1
    return count