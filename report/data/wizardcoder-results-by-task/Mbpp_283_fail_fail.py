# Task ID: Mbpp/283

# Description/Response:
"""
Write a python function takes in an integer and check whether the frequency of each digit in the integer is less than or equal to the digit itself.
assert validate(1234) == True
"""
def validate(n):
    digits = [int(d) for d in str(n)]
    for d in digits:
        if d > len(digits) or d > digits.count(d):
            return False
    return True