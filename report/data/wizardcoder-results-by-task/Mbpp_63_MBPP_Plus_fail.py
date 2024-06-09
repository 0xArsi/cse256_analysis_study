# Task ID: Mbpp/63

# Description/Response:
"""
Write a function to find the maximum difference between available pairs in the given tuple list.
assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7
"""
def max_difference(lst):
    max_diff = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            diff = abs(lst[i][1] - lst[j][0])
            if diff > max_diff:
                max_diff = diff
    return max_diff