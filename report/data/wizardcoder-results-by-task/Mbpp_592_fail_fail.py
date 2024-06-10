# Task ID: Mbpp/592

# Description/Response:
"""
Write a python function to find the sum of the product of consecutive binomial co-efficients.
assert sum_Of_product(3) == 15
"""
def sum_of_product(n):
    """
    This function takes an integer n as input and returns the sum of the product of consecutive binomial coefficients.
    """
    sum = 0
    for i in range(n):
        sum += (n-i)*i
    return sum