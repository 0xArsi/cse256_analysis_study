# Task ID: Mbpp/448

# Description/Response:
"""
Write a function to calculate the sum of perrin numbers.
assert cal_sum(9) == 49
"""
def cal_sum(n):
    """
    Calculates the sum of the first n Perrin numbers.
    
    Args:
    n (int): The number of Perrin numbers to sum.
    
    Returns:
    int: The sum of the first n Perrin numbers.
    """
    
    # Initialize the sum variable
    sum = 0
    
    # Loop through the first n Perrin numbers
    for i in range(1, n+1):
        # Calculate the value of each Perrin number
        perrin_num = i * (i + 1) * (i + 2) // 2
        
        # Add the value to the sum variable
        sum += perrin_num
        
    # Return the sum of the Perrin numbers
    return sum