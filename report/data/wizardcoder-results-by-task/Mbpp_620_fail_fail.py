# Task ID: Mbpp/620

# Description/Response:
"""
Write a function to find the size of the largest subset of a list of numbers so that every pair is divisible.
assert largest_subset([ 1, 3, 6, 13, 17, 18 ]) == 4
"""
def largest_subset(numbers):
    numbers.sort(reverse=True)
    subset = []
    largest = None
    for num in numbers:
        if largest is None or num % largest == 0:
            subset.append(num)
            largest = num
    return len(subset)