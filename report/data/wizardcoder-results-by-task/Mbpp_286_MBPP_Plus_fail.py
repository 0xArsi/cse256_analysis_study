# Task ID: Mbpp/286

# Description/Response:
"""
Write a function to find the largest sum of a contiguous array in the modified array which is formed by repeating the given array k times.
assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
"""
def max_sub_array_sum_repeated(arr, k, n):
    # repeat the array k times
    arr = arr * k
    # sort the array in descending order
    arr.sort(reverse=True)
    # initialize the sum of the first k elements to be the maximum sum
    max_sum = sum(arr[:k])
    # initialize the sum of the first k-1 elements to be 0
    prev_sum = 0
    # initialize the sum of the first k-1 elements to be 0
    curr_sum = 0
    # iterate over the array from the second element to the end
    for i in range(1, len(arr)):
        # add the current element to the previous sum
        curr_sum += arr[i]
        # if the current sum is greater than the previous sum, update the maximum sum
        if curr_sum > prev_sum:
            max_sum = curr_sum
        # update the previous sum to be the current sum
        prev_sum = curr_sum
    # return the maximum sum
    return max_sum