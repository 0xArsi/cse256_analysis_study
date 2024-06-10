# Task ID: Mbpp/644

# Description/Response:
"""
Write a python function to reverse an array upto a given position.
assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4) == [4, 3, 2, 1, 5, 6]
"""
def reverse_Array_Upto_K(arr, k):
    """
    Reverses the array up to the given position k
    """
    for i in range(k//2):
        arr[i], arr[k-i-1] = arr[k-i-1], arr[i]
    return arr