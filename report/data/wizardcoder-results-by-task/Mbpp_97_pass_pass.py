# Task ID: Mbpp/97

# Description/Response:
"""
Write a function to find frequency of each element in a flattened list of lists, returned in a dictionary.
assert frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]])=={1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}
"""
def frequency_lists(lst):
    freq = {}
    for sublist in lst:
        for item in sublist:
            if item in freq:
                freq[item] += 1
            else:
                freq[item] = 1
    return freq