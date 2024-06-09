# Task ID: Mbpp/398

# Description/Response:
"""
Write a function to compute the sum of digits of each number of a given list.
assert sum_of_digits([10,2,56])==14
"""
def sum_of_digits(lst):
    total = 0
    for num in lst:
        while num > 0:
            total += num % 10
            num //= 10
    return total