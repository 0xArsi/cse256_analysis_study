# Task ID: Mbpp/397

# Description/Response:
"""
Write a function to find the median of three numbers.
assert median_numbers(25,55,65)==55.0
"""
def median_numbers(a, b, c):
    """
    This function takes three numbers as input and returns their median value.
    """
    numbers = [a, b, c]
    numbers.sort()
    median = numbers[1]
    return median