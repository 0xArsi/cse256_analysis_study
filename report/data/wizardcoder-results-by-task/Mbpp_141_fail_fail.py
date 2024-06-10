# Task ID: Mbpp/141

# Description/Response:
"""
Write a function to sort a list of elements.
assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
"""
def pancake_sort(lst):
    n = len(lst)
    for i in range(n-1, 0, -1):
        # Find the index of the maximum element in the unsorted part of the list
        max_idx = 0
        for j in range(1, i+1):
            if lst[j] > lst[max_idx]:
                max_idx = j
        
        # Move the maximum element to the beginning of the list
        if max_idx != i:
            lst[0], lst[max_idx] = lst[max_idx], lst[0]
        
        # Reverse the unsorted part of the list
        lst[:i+1] = lst[:i+1][::-1]
        
    return lst