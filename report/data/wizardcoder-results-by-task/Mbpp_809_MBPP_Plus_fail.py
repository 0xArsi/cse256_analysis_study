# Task ID: Mbpp/809

# Description/Response:
"""
Write a function to check if each element of second tuple is smaller than its corresponding element in the first tuple.
assert check_smaller((1, 2, 3), (2, 3, 4)) == False
"""
def check_smaller(tup1, tup2):
    for i in range(len(tup1)):
        if tup1[i] > tup2[i]:
            return False
    return True