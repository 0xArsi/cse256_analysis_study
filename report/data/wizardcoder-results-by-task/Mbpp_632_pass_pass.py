# Task ID: Mbpp/632

# Description/Response:
"""
Write a python function to move all zeroes to the end of the given list.
assert move_zero([1,0,2,0,3,4]) == [1,2,3,4,0,0]
"""
def move_zero(lst):
    return [x for x in lst if x != 0] + [0] * lst.count(0)