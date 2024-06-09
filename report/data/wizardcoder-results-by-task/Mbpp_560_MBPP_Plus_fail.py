# Task ID: Mbpp/560

# Description/Response:
"""
Write a function to find the union of the elements of two given tuples and output them in sorted order.
assert union_elements((3, 4, 5, 6),(5, 7, 4, 10) ) == (3, 4, 5, 6, 7, 10)
"""
def union_elements(tup1, tup2):
    # Convert the tuples to sets to remove duplicates and then back to tuples
    return tuple(set(tup1).union(tup2))