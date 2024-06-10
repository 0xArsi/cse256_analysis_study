# Task ID: Mbpp/388

# Description/Response:
"""
Write a python function to find the highest power of 2 that is less than or equal to n.
assert highest_Power_of_2(10) == 8
"""
def highest_Power_of_2(n):
    power = 1
    while (power * 2 <= n):
        power *= 2
    return power