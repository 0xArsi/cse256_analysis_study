# Task ID: Mbpp/104

# Description/Response:
"""
Write a function to sort each sublist of strings in a given list of lists.
assert sort_sublists((["green", "orange"], ["black", "white"], ["white", "black", "orange"]))==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
"""
def sort_sublists(lst):
    return [sorted(sublist) for sublist in lst]