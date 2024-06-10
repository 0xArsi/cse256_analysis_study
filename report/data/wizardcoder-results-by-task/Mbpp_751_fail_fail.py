# Task ID: Mbpp/751

# Description/Response:
"""
Write a function to check if the given array represents min heap or not. 
assert check_min_heap([1, 2, 3, 4, 5, 6]) == True
"""
def check_min_heap(arr):
    n = len(arr)
    for i in range(n):
        if i >= 2*i+1 < n and arr[i] > arr[2*i+1]:
            return False
        if i >= 2*i+2 < n and arr[i] > arr[2*i+2]:
            return False
    return True