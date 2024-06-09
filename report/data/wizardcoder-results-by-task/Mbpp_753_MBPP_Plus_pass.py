# Task ID: Mbpp/753

# Description/Response:
"""
Write a function to find minimum k records from tuple list.  - in this case a verbatim copy of test cases
assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2) == [('Akash', 2), ('Akshat', 4)]
"""
def min_k(lst, k):
    return sorted(lst, key=lambda x: x[1])[:k]