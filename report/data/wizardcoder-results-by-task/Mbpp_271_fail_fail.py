# Task ID: Mbpp/271

# Description/Response:
"""
Write a python function that takes in an integer n and finds the sum of the first n even natural numbers that are raised to the fifth power.
assert even_Power_Sum(2) == 1056
"""
def even_Power_Sum(n):
    sum = 0
    for i in range(2, 2*n, 2):
        sum += i**5
    return sum