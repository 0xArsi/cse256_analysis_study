# Task ID: Mbpp/743

# Description/Response:
"""
Write a function to rotate a given list by specified number of items to the right direction. 
assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3)==[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
"""
def rotate_right(lst, n):
    """
    This function takes a list and a number n as input and returns the list rotated n items to the right.
    """
    n = n % len(lst) # To handle the case when n is greater than the length of the list
    return lst[-n:] + lst[:-n]