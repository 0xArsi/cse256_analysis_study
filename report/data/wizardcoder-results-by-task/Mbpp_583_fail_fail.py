# Task ID: Mbpp/583

# Description/Response:
"""
Write a function which returns nth catalan number.
assert catalan_number(10)==16796
"""
def catalan_number(n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return 0
    else:
        c = 1
        for i in range(1, 2 * n):
            c = c * (2 * n - i) // (i + 1)
        return c