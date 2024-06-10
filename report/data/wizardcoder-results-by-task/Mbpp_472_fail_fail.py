# Task ID: Mbpp/472

# Description/Response:
"""
Write a python function to check whether the given list contains consecutive numbers or not.
assert check_Consecutive([1,2,3,4,5]) == True
"""
def check_Consecutive(lst):
    """
    Checks if the given list contains consecutive numbers or not.
    
    Args:
    lst: a list of integers
    
    Returns:
    True if the list contains consecutive numbers, False otherwise.
    """
    
    # Sort the list in ascending order
    lst.sort()
    
    # Initialize variables to keep track of the current number and the difference between consecutive numbers
    prev_num = lst[0]
    diff = 1
    
    # Loop through the list starting from the second element
    for num in lst[1:]:
        # If the difference between the current number and the previous number is greater than 1, return False
        if num - prev_num > 1:
            return False
        
        # Update the previous number and the difference
        prev_num = num
        diff = num - prev_num
        
    # If the loop completes without returning False, return True
    return True