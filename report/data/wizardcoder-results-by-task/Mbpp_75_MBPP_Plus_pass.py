# Task ID: Mbpp/75

# Description/Response:
"""
Write a function to find tuples which have all elements divisible by k from the given list of tuples.
assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == [(6, 24, 12)]
"""
def find_tuples(lst, k):
    result = []
    for tup in lst:
        if all(x % k == 0 for x in tup):
            result.append(tup)
    return result