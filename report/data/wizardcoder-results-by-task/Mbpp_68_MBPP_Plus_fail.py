# Task ID: Mbpp/68

# Description/Response:
"""
Write a python function to check whether the given array is monotonic or not.
assert is_Monotonic([6, 5, 4, 4]) == True
"""
def is_monotonic(arr):
    """
    Check if the given array is monotonic.
    
    Parameters:
    arr (list): A list of integers.
    
    Returns:
    bool: True if the array is monotonic, False otherwise.
    """
    
    # Check if the array is sorted in ascending order
    if all(arr[i] <= arr[i+1] for i in range(len(arr)-1)):
        return True
    
    # Check if the array is sorted in descending order
    if all(arr[i] >= arr[i+1] for i in range(len(arr)-1)):
        return True
    
    # If the array is neither sorted in ascending nor descending order, it's not monotonic
    return False