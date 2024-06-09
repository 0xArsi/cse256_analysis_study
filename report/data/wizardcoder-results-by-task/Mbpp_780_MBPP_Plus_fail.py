# Task ID: Mbpp/780

# Description/Response:
"""
Write a function to find the combinations of sums with tuples in the given tuple list. 
assert find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]) == [(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)]
"""
def find_combinations(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            for k in range(j+1, len(lst)):
                for l in range(k+1, len(lst)):
                    result.append((lst[i][0] + lst[j][0] + lst[k][0] + lst[l][0], lst[i][1] + lst[j][1] + lst[k][1] + lst[l][1]))
    return result