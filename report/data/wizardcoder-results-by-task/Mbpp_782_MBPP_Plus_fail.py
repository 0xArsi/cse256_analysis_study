# Task ID: Mbpp/782

# Description/Response:
"""
Write a python function to find the sum of all odd length subarrays. 
assert odd_length_sum([1,2,4]) == 14
"""
def odd_length_sum(arr):
    n = len(arr)
    total = 0
    for i in range(n):
        for j in range(i+1, n):
            if j-i+1 % 2 == 1:
                total += sum(arr[i:j+1])
    return total