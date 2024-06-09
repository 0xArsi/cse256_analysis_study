# Task ID: Mbpp/604

# Description/Response:
"""
Write a function to reverse words seperated by spaces in a given string.
assert reverse_words("python program")==("program python")
"""
def reverse_words(string):
    words = string.split()
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)