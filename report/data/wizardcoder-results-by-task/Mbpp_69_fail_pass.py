# Task ID: Mbpp/69

# Description/Response:
"""
Write a function to check whether a list contains the given sublist or not.
assert is_sublist([2,4,3,5,7],[3,7])==False
"""
def is_sublist(lst, sublst):
    """
    Check if a list contains a sublist.
    
    Args:
    lst: the list to check
    sublst: the sublist to look for
    
    Returns:
    True if lst contains sublst, False otherwise
    """
    if not sublst:
        return True
    if not lst:
        return False
    if lst[0] == sublst[0]:
        return lst[1:] == sublst[1:] or is_sublist(lst[1:], sublst)
    return is_sublist(lst[1:], sublst)