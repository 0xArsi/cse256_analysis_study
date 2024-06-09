# Task ID: Mbpp/803

# Description/Response:
"""
Write a function to check whether the given number is a perfect square or not. 
assert not is_perfect_square(10)
"""
def is_perfect_square(n):
    if n < 0:
        return False
    else:
        root = int(n ** 0.5)
        return root * root == n