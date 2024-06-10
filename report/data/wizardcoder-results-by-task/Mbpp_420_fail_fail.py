# Task ID: Mbpp/420

# Description/Response:
"""
Write a python function to find the cube sum of first n even natural numbers.
assert cube_Sum(2) == 72
"""
def cube_Sum(n):
    sum = 0
    for i in range(1, n+1, 2):
        sum += i**3
    return sum