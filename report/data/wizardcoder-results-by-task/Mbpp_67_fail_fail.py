# Task ID: Mbpp/67

# Description/Response:
"""
Write a function to find the number of ways to partition a set of Bell numbers.
assert bell_number(2)==2
"""
def bell_number(n):
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return bell_number(n-1) + bell_number(n-2)