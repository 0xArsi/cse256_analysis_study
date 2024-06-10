# Task ID: Mbpp/597

# Description/Response:
"""
Write a function to find kth element from the given two sorted arrays.
assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
"""
def find_kth(arr1, arr2, k):
    """
    Find the kth element from the given two sorted arrays.
    """
    if k > len(arr1) + len(arr2):
        return None
    elif k <= len(arr1):
        return arr1[k-1]
    else:
        return arr2[k - len(arr1) - 1]