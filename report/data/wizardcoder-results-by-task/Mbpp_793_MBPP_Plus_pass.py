# Task ID: Mbpp/793

# Description/Response:
"""
Write a python function to find the last position of an element in a sorted array.
assert last([1,2,3],1) == 0
"""
def last(arr, x):
    """
    Returns the last position of an element in a sorted array.
    If the element is not found, returns -1.
    """
    n = len(arr)
    l = 0
    r = n - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == x:
            if mid == n - 1 or arr[mid + 1] != x:
                return mid
            else:
                l = mid + 1
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1