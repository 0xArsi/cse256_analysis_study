# Task ID: Mbpp/577

# Description/Response:
"""
Write a python function to find the last digit in factorial of a given number.
assert last_Digit_Factorial(4) == 4
"""
def last_Digit_Factorial(n):
    if n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n+1):
            fact *= i
        return fact % 10