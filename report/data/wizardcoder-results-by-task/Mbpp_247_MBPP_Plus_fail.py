# Task ID: Mbpp/247

# Description/Response:
"""
Write a function to find the length of the longest palindromic subsequence in the given string.
assert lps("TENS FOR TENS") == 5
"""
def lps(s):
    n = len(s)
    dp = [[0 for x in range(n)] for x in range(n)]
    
    for i in range(n):
        dp[i][i] = 1
    
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = 2
    
    for k in range(2, n):
        for i in range(n-k):
            j = i+k
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    
    return dp[0][n-1]