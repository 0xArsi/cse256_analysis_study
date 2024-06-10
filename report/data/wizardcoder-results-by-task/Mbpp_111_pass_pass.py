# Task ID: Mbpp/111

# Description/Response:
"""
Write a function to find the common elements in given nested lists.
assert set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))==set([18, 12])
"""
def common_in_nested_lists(lists):
    common = set()
    for lst in lists:
        for elem in lst:
            if all(elem in lst2 for lst2 in lists):
                common.add(elem)
    return common