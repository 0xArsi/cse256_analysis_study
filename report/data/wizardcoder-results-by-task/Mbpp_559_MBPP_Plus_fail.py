# Task ID: Mbpp/559

# Description/Response:
"""
Write a function to find the sum of the largest contiguous sublist in the given list.
assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7
"""
def max_sub_array_sum(arr):
    max_sum = float('-inf')
    current_sum = 0
    max_start = 0
    max_end = 0
    start = 0
    end = 0
    temp_sum = 0
    
    for i, num in enumerate(arr):
        if current_sum <= 0:
            current_sum = num
            start = i
        else:
            current_sum += num
        
        if current_sum > max_sum:
            max_sum = current_sum
            max_start = start
            max_end = i
        
        if i == len(arr) - 1:
            if current_sum > temp_sum:
                temp_sum = current_sum
    
    return temp_sum