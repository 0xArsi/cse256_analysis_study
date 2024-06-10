# Task ID: Mbpp/633

# Description/Response:
"""
Write a python function to find the sum of xor of all pairs of numbers in the given list.
assert pair_xor_Sum([5,9,7,6],4) == 47
"""
def pair_xor_Sum(lst, k):
    """
    This function takes a list of integers and an integer k as input and returns the sum of xor of all pairs of numbers in the list.
    """
    # Initialize the sum variable to 0
    sum = 0
    # Loop through the list
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            # Calculate the xor of the current pair of numbers and add it to the sum
            sum += lst[i] ^ lst[j]
    # Add k to the sum
    sum += k
    # Return the sum
    return sum