# Task ID: Mbpp/445

# Description/Response:
"""
Write a function to perform index wise multiplication of tuple elements in the given two tuples.
assert index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3)) ) == ((6, 21), (12, 45), (2, 9), (7, 30))
"""
def index_multiplication(tup1, tup2):
    result = []
    for i in range(len(tup1)):
        result.append(tup1[i] * tup2[i])
    return tuple(result)