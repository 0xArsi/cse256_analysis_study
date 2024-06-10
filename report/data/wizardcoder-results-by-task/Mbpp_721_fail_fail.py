# Task ID: Mbpp/721

# Description/Response:
"""
Given a square matrix of size N*N given as a list of lists, where each cell is associated with a specific cost. A path is defined as a specific sequence of cells that starts from the top-left cell move only right or down and ends on bottom right cell. We want to find a path with the maximum average over all existing paths. Average is computed as total cost divided by the number of cells visited in the path.
assert maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]) == 5.2
"""
def maxAverageOfPath(matrix):
    n = len(matrix)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == 0 or j == 0:
                dp[i][j] = matrix[i][j]
            elif i == j == 0:
                dp[i][j] = matrix[i][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + matrix[i][j]
    max_avg = max(dp[i][-1], dp[-1][j])
    return max_avg / (n - 1)

# Test the function