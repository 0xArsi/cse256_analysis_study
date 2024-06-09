# Task ID: Mbpp/239

# Description/Response:
"""
Write a function that takes in positive integers m and n and finds the number of possible sequences of length n, such that each element is a positive integer and is greater than or equal to twice the previous element but less than or equal to m.
assert get_total_number_of_sequences(10, 4) == 4
"""
def get_total_number_of_sequences(m, n):
    if n == 1:
        return 1
    elif n == 2:
        return m - 1
    else:
        return (m - 2) * (m - 3) // 2