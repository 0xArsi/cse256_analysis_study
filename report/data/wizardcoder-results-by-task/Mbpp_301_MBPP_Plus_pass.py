# Task ID: Mbpp/301

# Description/Response:
"""
Write a function to find the depth of a dictionary.
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
"""
def dict_depth(d):
    if not isinstance(d, dict):
        return 0
    elif not d:
        return 1
    else:
        return 1 + max(dict_depth(v) for v in d.values())