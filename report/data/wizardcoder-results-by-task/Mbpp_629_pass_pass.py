# Task ID: Mbpp/629

# Description/Response:
"""
Write a python function to find even numbers from a list of numbers.
assert Split([1,2,3,4,5]) == [2,4]
"""
def Split(lst):
    even_numbers = []
    for num in lst:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers