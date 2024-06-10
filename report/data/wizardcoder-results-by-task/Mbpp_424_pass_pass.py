# Task ID: Mbpp/424

# Description/Response:
"""
Write a function to extract only the rear index element of each string in the given tuple.
assert extract_rear(('Mers', 'for', 'Vers') ) == ['s', 'r', 's']
"""
def extract_rear(lst):
    return [s[-1] for s in lst]