# Task ID: Mbpp/463

# Description/Response:
"""
Write a function to find the maximum product subarray of the given array.
assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
"""
def max_subarray_product(arr):
    max_product = float('-inf')
    min_product = float('-inf')
    max_so_far = float('-inf')
    min_so_far = float('-inf')
    max_ending_here = float('-inf')
    min_ending_here = float('-inf')
    
    for num in arr:
        if num < 0:
            max_product = max(max_product, min_product * num)
            min_product = min(min_product * num, num)
        else:
            max_product = max(max_product, num)
            min_product = max(min_product, num)
        
        max_ending_here = max(max_ending_here * num, num)
        min_ending_here = min(min_ending_here * num, num)
        
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
        
        if min_ending_here < min_so_far:
            min_so_far = min_ending_here
    
    return max_so_far