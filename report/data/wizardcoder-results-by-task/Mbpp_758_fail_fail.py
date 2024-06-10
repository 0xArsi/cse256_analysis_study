# Task ID: Mbpp/758

# Description/Response:
"""
Write a function to count lists within a list. The function should return a dictionary where every list is converted to a tuple and the value of such tuple is the number of its occurencies in the original list.
assert unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]] )=={(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
"""
def count_sublists(lst):
    sublists = {}
    for sublist in lst:
        sublist_tuple = tuple(sublist)
        if sublist_tuple in sublists:
            sublists[sublist_tuple] += 1
        else:
            sublists[sublist_tuple] = 1
    return sublists