# Task ID: Mbpp/92

# Description/Response:
"""
Write a function to check whether the given number is undulating or not.
assert is_undulating(1212121) == True
"""
def is_undulating(n):
    """
    Check whether a number is undulating or not.
    
    A number is considered undulating if it has the same digits in both odd and even positions, and the digits differ by at least 1.
    
    Args:
    n (int): The number to check.
    
    Returns:
    bool: True if the number is undulating, False otherwise.
    """
    n_str = str(n)
    for i in range(len(n_str) // 2):
        if n_str[i] != n_str[len(n_str) - 1 - i]:
            return False
    return True