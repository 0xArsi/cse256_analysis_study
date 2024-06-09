# Task ID: Mbpp/168

# Description/Response:
"""
Write a function to count the number of occurrences of a number in a given list.
assert frequency([1,2,3], 4) == 0
"""
def frequency(lst, num):
    count = 0
    for i in lst:
        if i == num:
            count += 1
    return count