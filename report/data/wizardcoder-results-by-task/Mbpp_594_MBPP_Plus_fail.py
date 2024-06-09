# Task ID: Mbpp/594

# Description/Response:
"""
Write a function to find the difference of the first even and first odd number of a given list.
assert diff_even_odd([1,3,5,7,4,1,6,8])==3
"""
def diff_even_odd(lst):
    even = None
    odd = None
    for num in lst:
        if num % 2 == 0:
            even = num
            break
    for num in lst:
        if num % 2 != 0:
            odd = num
            break
    return abs(even - odd)