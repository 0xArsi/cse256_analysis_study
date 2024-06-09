# Task ID: Mbpp/138

# Description/Response:
"""
Write a python function to check whether the given number can be represented as sum of non-zero powers of 2 or not.
assert is_Sum_Of_Powers_Of_Two(10) == True
"""
def is_Sum_Of_Powers_Of_Two(n):
    """
    This function takes an integer n as input and returns True if it can be represented as sum of non-zero powers of 2, else False.
    """
    # Initialize a variable to store the sum of powers of 2
    sum_of_powers = 0
    
    # Initialize a variable to store the power of 2
    power = 1
    
    # Loop through all powers of 2 from 1 to n
    while power <= n:
        # If the current power of 2 is a factor of n, add it to the sum_of_powers
        if n % power == 0:
            sum_of_powers += power
            n //= power
        else:
            # If the current power of 2 is not a factor of n, increment the power by 1
            power += 1
    
    # If the sum of powers of 2 is equal to n, return True, else False
    return sum_of_powers == n