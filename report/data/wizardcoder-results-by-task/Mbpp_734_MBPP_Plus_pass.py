# Task ID: Mbpp/734

# Description/Response:
"""
Write a python function to find sum of products of all possible sublists of a given list. 
assert sum_Of_Subarray_Prod([1,2,3]) == 20
"""
def sum_Of_Subarray_Prod(arr):
    n = len(arr)
    total_sum = 0
    for i in range(n):
        for j in range(i, n):
            prod = 1
            for k in range(i, j+1):
                prod *= arr[k]
            total_sum += prod
    return total_sum