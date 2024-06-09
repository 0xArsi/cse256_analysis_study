# Task ID: Mbpp/129

# Description/Response:
"""
Write a function to calculate whether the matrix is a magic square.
assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
"""
def magic_square_test(matrix):
    n = len(matrix)
    magic_sum = 0
    for i in range(n):
        magic_sum += matrix[i][i]
    for j in range(n):
        magic_sum -= matrix[j][n-1-j]
    if magic_sum != sum(range(1, n**2+1)):
        return False
    for i in range(n):
        row_sum = sum(matrix[i])
        if row_sum != magic_sum:
            return False
        col_sum = sum([matrix[j][i] for j in range(n)]
        if col_sum != magic_sum:
            return False
    return True