# Task ID: Mbpp/70

# Description/Response:
"""
Write a function to find whether all the given tuples have equal length or not.
assert get_equal([(11, 22, 33), (44, 55, 66)]) == True
"""
def get_equal(tuples):
    """
    This function takes a list of tuples as input and returns True if all the tuples have equal length, else False.
    """
    if len(set(map(len, tuples)) == 1:
        return True
    else:
        return False