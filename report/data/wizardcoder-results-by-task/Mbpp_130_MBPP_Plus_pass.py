# Task ID: Mbpp/130

# Description/Response:
"""
Write a function to find the item with maximum frequency in a given list.
assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])==2
"""
def max_occurrences(lst):
    freq_dict = {}
    for item in lst:
        if item in freq_dict:
            freq_dict[item] += 1
        else:
            freq_dict[item] = 1
    max_freq = 0
    max_item = None
    for item, count in freq_dict.items():
        if count > max_freq:
            max_freq = count
            max_item = item
    return max_item