# Task ID: Mbpp/462

# Description/Response:
"""
Write a function to find all possible combinations of the elements of a given list.
assert combinations_list(['orange', 'red', 'green', 'blue'])==[[], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green', 'red'], ['green', 'red', 'orange'], ['blue'], ['blue', 'orange'], ['blue', 'red'], ['blue', 'red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green', 'red'], ['blue', 'green', 'red', 'orange']]
"""
def combinations_list(lst):
    if len(lst) == 0:
        return [[]]
    else:
        rest = combinations_list(lst[1:])
        return [[]] + [x+[lst[0]] for x in rest] + [x+[lst[0]]+y for x in rest for y in combinations_list(lst[1:])]