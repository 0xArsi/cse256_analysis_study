# Task ID: Mbpp/90

# Description/Response:
"""
Write a python function to find the length of the longest word.
assert len_log(["python","PHP","bigdata"]) == 7
"""
def len_log(words):
    max_length = 0
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
    return max_length