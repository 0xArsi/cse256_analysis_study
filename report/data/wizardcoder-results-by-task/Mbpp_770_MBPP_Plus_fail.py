# Task ID: Mbpp/770

# Description/Response:
"""
Write a python function to find the sum of fourth power of first n odd natural numbers.
assert odd_num_sum(2) == 82
"""
def odd_num_sum(n):
    sum = 0
    for i in range(1, n+1, 2):
        sum += i**4
    return sum