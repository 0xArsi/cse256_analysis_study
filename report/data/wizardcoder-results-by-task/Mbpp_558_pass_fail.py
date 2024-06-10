# Task ID: Mbpp/558

# Description/Response:
"""
Write a python function to find the sum of the per-digit difference between two integers.
assert digit_distance_nums(1,2) == 1
"""
def digit_distance_nums(num1, num2):
    """
    This function takes two integers as input and returns the sum of the per-digit difference between them.
    """
    # Convert the integers to strings to be able to iterate over each digit
    num1_str = str(num1)
    num2_str = str(num2)
    
    # Initialize the sum variable to 0
    sum = 0
    
    # Iterate over the digits of the first number and subtract the corresponding digit of the second number
    for i in range(len(num1_str)):
        sum += abs(int(num1_str[i]) - int(num2_str[i]))
    
    return sum