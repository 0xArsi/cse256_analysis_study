# Task ID: Mbpp/639

# Description/Response:
"""
Write a function to sum the length of the names of a given list of names after removing the names that start with a lowercase letter.
assert sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])==16
"""
def sum_names(names):
    total_length = 0
    for name in names:
        if name[0].isupper():
            total_length += len(name)
    return total_length