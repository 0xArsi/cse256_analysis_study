# Task ID: Mbpp/801

# Description/Response:
"""
Write a python function to count the number of equal numbers from three given integers.
assert test_three_equal(1,1,1) == 3
"""
def test_three_equal(a, b, c):
    count = 0
    if a == b and b == c:
        count += 1
    if a != b and b == c:
        count += 1
    if a == b and b != c:
        count += 1
    if a != b and b != c and a == c:
        count += 1
    if a != b and b != c and a != c:
        count += 1
    return count