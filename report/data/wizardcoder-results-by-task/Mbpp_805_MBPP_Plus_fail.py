# Task ID: Mbpp/805

# Description/Response:
"""
Write a function that returns the list in a list of lists whose sum of elements is the highest.
assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12]
"""
def max_sum_list(lst):
    max_sum = 0
    max_lst = []
    for l in lst:
        if sum(l) > max_sum:
            max_sum = sum(l)
            max_lst = l
    return max_lst