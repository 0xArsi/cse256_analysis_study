# Task ID: Mbpp/128

# Description/Response:
"""
Write a function to find words that are longer than n characters from a given list of words.
assert long_words(3,"python is a programming language")==['python','programming','language']
"""
def long_words(n, sentence):
    words = sentence.split()
    long_words = []
    for word in words:
        if len(word) > n:
            long_words.append(word)
    return long_words