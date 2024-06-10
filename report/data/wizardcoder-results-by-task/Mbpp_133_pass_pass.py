# Task ID: Mbpp/133

# Description/Response:
"""
Write a function to calculate the sum of the negative numbers of a given list of numbers.
assert sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17])==-32
"""
def sum_negativenum(lst):
    """
    This function takes a list of numbers as input and returns the sum of negative numbers in the list.
    """
    neg_sum = 0
    for num in lst:
        if num < 0:
            neg_sum += num
    return neg_sum