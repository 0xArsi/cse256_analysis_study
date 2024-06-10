# Task ID: Mbpp/763

# Description/Response:
"""
Write a python function to find the minimum difference between any two elements in a given array. 
assert find_min_diff((1,5,3,19,18,25),6) == 1
"""
def find_min_diff(arr, k):
    arr.sort()
    min_diff = float('inf')
    for i in range(len(arr)-1):
        diff = arr[i+1] - arr[i]
        if diff < min_diff:
            min_diff = diff
    return min_diff