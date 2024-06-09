# Task ID: Mbpp/740

# Description/Response:
"""
Write a function to convert the given tuple to a key-value dictionary using adjacent elements. 
assert tuple_to_dict((1, 5, 7, 10, 13, 5)) == {1: 5, 7: 10, 13: 5}
"""
def tuple_to_dict(tup):
    """
    This function takes a tuple as input and returns a dictionary with adjacent elements as key-value pairs.
    """
    result = {}
    for i in range(0, len(tup), 2):
        result[tup[i]] = tup[i+1]
    return result