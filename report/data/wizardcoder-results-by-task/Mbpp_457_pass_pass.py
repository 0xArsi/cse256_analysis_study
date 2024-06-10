# Task ID: Mbpp/457

# Description/Response:
"""
Write a python function to find the sublist having minimum length.
assert Find_Min([[1],[1,2],[1,2,3]]) == [1]
"""
def Find_Min(lst):
    if not lst:
        return []
    min_len = len(lst[0])
    min_sublist = lst[0]
    for sublist in lst:
        if len(sublist) < min_len:
            min_len = len(sublist)
            min_sublist = sublist
    return min_sublist