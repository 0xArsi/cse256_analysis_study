# Task ID: Mbpp/579

# Description/Response:
"""
Write a function to find the dissimilar elements in the given two tuples.
assert find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)) == (3, 6, 7, 10)
"""
def find_dissimilar(t1, t2):
    """
    Given two tuples t1 and t2, returns a tuple of all elements that are different between them.
    """
    dissimilar = []
    for i in range(len(t1)):
        if t1[i] != t2[i]:
            dissimilar.append(t1[i])
    for i in range(len(t2)):
        if t2[i] not in t1:
            dissimilar.append(t2[i])
    return tuple(dissimilar)