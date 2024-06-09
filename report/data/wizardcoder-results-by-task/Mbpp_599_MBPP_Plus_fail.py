# Task ID: Mbpp/599

# Description/Response:
"""
Write a function to find sum and average of first n natural numbers.
assert sum_average(10)==(55, 5.5)
"""
def sum_average(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return (total, total/n)