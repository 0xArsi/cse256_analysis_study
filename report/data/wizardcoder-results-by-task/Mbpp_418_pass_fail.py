# Task ID: Mbpp/418

# Description/Response:
"""
Write a python function to find the element of a list having maximum length.
assert Find_Max([['A'],['A','B'],['A','B','C']]) == ['A','B','C']
"""
def Find_Max(lst):
    max_length = 0
    max_element = []
    for i in lst:
        if len(i) > max_length:
            max_length = len(i)
            max_element = i
        elif len(i) == max_length:
            max_element.append(i)
    return max_element