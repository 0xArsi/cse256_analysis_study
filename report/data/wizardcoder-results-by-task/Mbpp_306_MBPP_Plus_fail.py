# Task ID: Mbpp/306

# Description/Response:
"""
Write a function to find the maximum sum of increasing subsequence from prefix until ith index and also including a given kth element which is after i, i.e., k > i .
assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
"""
def max_sum_increasing_subseq(arr, i, k, x):
    n = len(arr)
    if i >= n or k >= n or i > k:
        return None
    
    dp = [0] * n
    dp[0] = arr[0]
    
    for j in range(1, n):
        dp[j] = max(dp[j-1], arr[j])
    
    for j in range(1, n):
        for l in range(j):
            if arr[j] > arr[l]:
                dp[j] = max(dp[j], dp[l] + arr[j])
    
    max_sum = dp[i]
    
    for j in range(i+1, k):
        max_sum = max(max_sum, dp[j])
    
    return max_sum + x