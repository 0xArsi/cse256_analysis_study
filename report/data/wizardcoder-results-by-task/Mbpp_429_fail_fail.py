# Task ID: Mbpp/429

# Description/Response:
"""
Write a function to extract the elementwise and tuples from the given two tuples.
assert and_tuples((10, 4, 6, 9), (5, 2, 3, 3)) == (0, 0, 2, 1)
"""
def and_tuples(t1, t2):
    return tuple(t1[i] & t2[i] for i in range(len(t1))), tuple(t1[i] ^ t2[i] for i in range(len(t1)))