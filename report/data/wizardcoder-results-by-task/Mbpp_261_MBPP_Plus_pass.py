# Task ID: Mbpp/261

# Description/Response:
"""
Write a function that takes in two tuples and performs mathematical division operation element-wise across the given tuples.
assert division_elements((10, 4, 6, 9),(5, 2, 3, 3)) == (2, 2, 2, 3)
"""
def division_elements(tup1, tup2):
    return tuple(map(lambda x, y: x/y, tup1, tup2))