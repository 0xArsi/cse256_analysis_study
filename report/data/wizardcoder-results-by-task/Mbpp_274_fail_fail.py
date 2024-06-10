# Task ID: Mbpp/274

# Description/Response:
"""
Write a python function that takes in a positive integer n and finds the sum of even index binomial coefficients.
assert even_binomial_Coeff_Sum(4) == 8
"""
def even_binomial_Coeff_Sum(n):
    sum = 0
    for i in range(0, n+1):
        sum += binomial(n, i) if i % 2 == 0 else 0
    return sum