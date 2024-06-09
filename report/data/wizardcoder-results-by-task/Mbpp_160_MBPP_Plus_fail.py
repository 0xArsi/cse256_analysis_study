# Task ID: Mbpp/160

# Description/Response:
"""
Write a function that returns integers x and y that satisfy ax + by = n as a tuple, or return None if no solution exists.
assert find_solution(2, 3, 7) == (2, 1)
"""
def find_solution(a, b, n):
    if n % a == 0:
        return (n // a, 0)
    elif n % b == 0:
        return (0, n // b)
    else:
        return None