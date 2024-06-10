# Task ID: Mbpp/290

# Description/Response:
"""
Write a function to find the list of maximum length in a list of lists.
assert max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(3, [13, 15, 17])
"""
def max_length(lst):
    max_len = 0
    max_lst = []
    for sublst in lst:
        if len(sublst) > max_len:
            max_len = len(sublst)
            max_lst = sublst
    return max_len, max_lst