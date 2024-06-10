# Task ID: Mbpp/470

# Description/Response:
"""
Write a function to find the pairwise addition of the neighboring elements of the given tuple.
assert add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)
"""
def add_pairwise(tup):
    """
    Given a tuple of integers, returns a tuple of the pairwise addition of the neighboring elements.
    """
    result = ()
    for i in range(len(tup)-1):
        result += (tup[i] + tup[i+1],)
    return result