# Task ID: Mbpp/414

# Description/Response:
"""
Write a python function to check whether any value in a sequence exists in a sequence or not.
assert overlapping([1,2,3,4,5],[6,7,8,9]) == False
"""
def overlapping(seq1, seq2):
    for val in seq1:
        if val in seq2:
            return True
    return False