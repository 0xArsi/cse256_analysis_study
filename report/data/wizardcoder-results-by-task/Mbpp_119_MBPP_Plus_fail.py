# Task ID: Mbpp/119

# Description/Response:
"""
Write a python function to find the element that appears only once in a sorted array.
assert search([1,1,2,2,3]) == 3
"""
def search(arr):
    n = len(arr)
    if n % 2 == 0:
        return None
    
    for i in range(0, n, 2):
        if arr[i] != arr[i+1]:
            return arr[i]
    
    return None