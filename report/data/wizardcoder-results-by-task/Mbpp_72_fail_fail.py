# Task ID: Mbpp/72

# Description/Response:
"""
Write a python function to check whether the given number can be represented as the difference of two squares or not.
assert dif_Square(5) == True
"""
def dif_Square(n):
    for i in range(1, int(n**0.5)+1):
        for j in range(1, int(n**0.5)+1):
            if i**2 + j**2 == n:
                return True
    return False