# Task ID: Mbpp/140

# Description/Response:
"""
Write a function to flatten the list of lists into a single set of numbers.
assert set(extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)])) == set([3, 4, 5, 7, 1])
"""
def extract_singly(lst):
    flat_list = []
    for sublist in lst:
        for item in sublist:
            flat_list.append(item)
    return set(flat_list)