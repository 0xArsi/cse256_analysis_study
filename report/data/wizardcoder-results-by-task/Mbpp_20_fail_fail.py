# Task ID: Mbpp/20

# Description/Response:
"""
Write a function to check if the given number is woodball or not.
assert is_woodall(383) == True
"""
def is_woodall(n):
    # Convert the number to a string and split it into digits
    digits = [int(d) for d in str(n)]
    # Check if the sum of the digits is equal to the product of the digits
    return sum(digits) == n * len(digits)