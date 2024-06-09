# Task ID: Mbpp/453

# Description/Response:
"""
Write a python function to find the sum of even factors of a number.
assert sumofFactors(18) == 26
"""
def sumofFactors(n):
    factors = []
    for i in range(1, n+1):
        if n % i == 0:
            if i % 2 == 0:
                factors.append(i)
    return sum(factors)