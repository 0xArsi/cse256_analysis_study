# Task ID: Mbpp/259

# Description/Response:
"""
Write a function to maximize the given two tuples.
assert maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))) == ((6, 7), (4, 9), (2, 9), (7, 10))
"""
def maximize_elements(t1, t2):
    result = []
    for i in range(len(t1)):
        if t1[i][1] > t2[i][1]:
            result.append(t1[i])
        else:
            result.append(t2[i])
    return tuple(result)