# Task ID: Mbpp/733

# Description/Response:
"""
Write a function to find the index of the first occurrence of a given number in a sorted array.
assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1
"""
def find_first_occurrence(arr, num):
    """
    Find the index of the first occurrence of a given number in a sorted array.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == num:
            if mid == 0 or arr[mid - 1] != num:
                return mid
            right = mid - 1
        elif arr[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return -1