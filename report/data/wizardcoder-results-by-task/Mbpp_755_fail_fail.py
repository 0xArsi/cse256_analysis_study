# Task ID: Mbpp/755

# Description/Response:
"""
Write a function to find the second smallest number in a list.
assert second_smallest([1, 2, -8, -2, 0, -2])==-2
"""
def second_smallest(lst):
    # Find the smallest number in the list
    smallest = min(lst)
    # Remove the smallest number from the list
    lst.remove(smallest)
    # Find the smallest number in the remaining list
    second_smallest = min(lst)
    return second_smallest