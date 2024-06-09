# Task ID: Mbpp/421

# Description/Response:
"""
Write a function to concatenate each element of tuple by the delimiter.
assert concatenate_tuple(("ID", "is", 4, "UTS") ) == 'ID-is-4-UTS'
"""
def concatenate_tuple(tup, delimiter='-'):
    return delimiter.join(str(x) for x in tup)