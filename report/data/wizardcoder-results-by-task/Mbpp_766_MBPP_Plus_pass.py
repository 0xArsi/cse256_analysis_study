# Task ID: Mbpp/766

# Description/Response:
"""
Write a function to return a list of all pairs of consecutive items in a given list.
assert pair_wise([1,1,2,3,3,4,4,5])==[(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]
"""
def pair_wise(lst):
    pairs = []
    for i in range(len(lst)-1):
        pairs.append((lst[i], lst[i+1]))
    return pairs