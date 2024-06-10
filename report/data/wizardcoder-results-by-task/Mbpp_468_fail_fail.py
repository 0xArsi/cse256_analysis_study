# Task ID: Mbpp/468

# Description/Response:
"""
Write a function to find the maximum product formed by multiplying numbers of an increasing subsequence of that array.
assert max_product([3, 100, 4, 5, 150, 6]) == 3000
"""
def max_product(arr):
    n = len(arr)
    if n == 0:
        return 0
    elif n == 1:
        return arr[0]
    elif n == 2:
        return max(arr[0], arr[1])
    else:
        max_ending_here = [0] * n
        max_so_far = [0] * n
        max_ending_here[0] = arr[0]
        max_ending_here[1] = max(arr[0], arr[1])
        max_so_far[0] = max_ending_here[0]
        max_so_far[1] = max_ending_here[1]
        for i in range(2, n):
            max_ending_here[i] = max(max_ending_here[i-1] * arr[i], arr[i])
            max_so_far[i] = max(max_so_far[i-1], max_ending_here[i])
        return max_so_far[-1]