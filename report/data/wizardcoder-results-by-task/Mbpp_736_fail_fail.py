# Task ID: Mbpp/736

# Description/Response:
"""
Write a function to locate the left insertion point for a specified value in sorted order. 
assert left_insertion([1,2,4,5],6)==4
"""
def left_insertion(arr, val):
    """
    Returns the left insertion point for a specified value in a sorted array.
    """
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < val:
            left = mid + 1
        else:
            right = mid
    return left