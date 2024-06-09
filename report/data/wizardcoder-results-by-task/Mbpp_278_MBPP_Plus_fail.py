# Task ID: Mbpp/278

# Description/Response:
"""
Write a function to find the number of elements that occurs before the tuple element in the given tuple.
assert count_first_elements((1, 5, 7, (4, 6), 10) ) == 3
"""
def count_first_elements(t):
    count = 0
    for element in t:
        if not isinstance(element, tuple):
            count += 1
        else:
            count += count_first_elements(element)
    return count