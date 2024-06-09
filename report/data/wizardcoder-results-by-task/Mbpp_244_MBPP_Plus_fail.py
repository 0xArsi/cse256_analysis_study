# Task ID: Mbpp/244

# Description/Response:
"""
Write a python function to find the next perfect square greater than a given number.
assert next_Perfect_Square(35) == 36
"""
def next_Perfect_Square(num):
    """
    This function takes a number as input and returns the next perfect square greater than the input number.
    """
    # Calculate the square root of the input number
    sqrt_num = int(num ** 0.5)
    # If the square root is an integer, return the next perfect square
    if sqrt_num ** 2 == num:
        return (sqrt_num + 1) ** 2
    # If the square root is not an integer, return the next integer square
    else:
        return (sqrt_num + 1) ** 2