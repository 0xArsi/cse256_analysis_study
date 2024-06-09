# Task ID: Mbpp/251

# Description/Response:
"""
Write a function that takes in a list and an element and inserts the element before each element in the list, and returns the resulting list.
assert insert_element(['Red', 'Green', 'Black'] ,'c')==['c', 'Red', 'c', 'Green', 'c', 'Black']
"""
def insert_element(lst, elem):
    new_lst = []
    for i in range(len(lst)):
        new_lst.append(elem)
        new_lst.append(lst[i])
    return new_lst