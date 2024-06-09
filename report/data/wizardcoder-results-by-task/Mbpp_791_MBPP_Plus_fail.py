# Task ID: Mbpp/791

# Description/Response:
"""
Write a function to remove tuples from the given tuple.
assert remove_nested((1, 5, 7, (4, 6), 10)) == (1, 5, 7, 10)
"""
def remove_nested(tup):
    result = []
    for item in tup:
        if type(item) == tuple:
            result.extend(item)
        else:
            result.append(item)
    return tuple(result)