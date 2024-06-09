# Task ID: Mbpp/296

# Description/Response:
"""
Write a python function to count inversions in an array.
assert get_Inv_Count([1,20,6,4,5]) == 5
"""
def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    
    mid = len(arr) // 2
    left, inv_left = merge_sort(arr[:mid])
    right, inv_right = merge_sort(arr[mid:])
    
    merged, inv_merge = merge(left, right)
    return merged, inv_left + inv_right + inv_merge
    
def merge(left, right):
    i = j = inv = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            inv += len(left) - i
            j += 1
    
    result += left[i:]
    result += right[j:]
    
    return result, inv

def get_Inv_Count(arr):
    sorted_arr, inv_count = merge_sort(arr)
    return inv_count