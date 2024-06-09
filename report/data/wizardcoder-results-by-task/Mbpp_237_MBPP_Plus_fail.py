# Task ID: Mbpp/237

# Description/Response:
"""
Write a function that takes in a list of tuples and returns a dictionary mapping each unique tuple to the number of times it occurs in the list.
assert check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)] ) == {(1, 3): 2, (2, 5): 2, (3, 6): 1}
"""
def count_tuples(lst):
    counts = {}
    for tup in lst:
        if tup in counts:
            counts[tup] += 1
        else:
            counts[tup] = 1
    return counts