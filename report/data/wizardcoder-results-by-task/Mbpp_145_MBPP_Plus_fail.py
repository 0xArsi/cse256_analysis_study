# Task ID: Mbpp/145

# Description/Response:
"""
Write a python function to find the maximum difference between any two elements in a given array.
assert max_Abs_Diff((2,1,5,3)) == 4
"""
def max_Abs_Diff(arr):
    return max(abs(arr[i] - arr[j]) for i in range(len(arr)) for j in range(len(arr)) if i != j)