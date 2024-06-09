# Task ID: Mbpp/84

# Description/Response:
"""
Write a function to find the nth number in the newman conway sequence.
assert sequence(10) == 6
"""
def sequence(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        a = 0
        b = 1
        c = 1
        for i in range(3, n+1):
            d = a + b
            a = b
            b = c
            c = d
        return c