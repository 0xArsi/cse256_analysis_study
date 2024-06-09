# Task ID: Mbpp/439

# Description/Response:
"""
Write a function to join a list of multiple integers into a single integer.
assert multiple_to_single([11, 33, 50])==113350
"""
def multiple_to_single(lst):
    result = 0
    for num in lst:
        result = result * 10 + num
    return result