# Task ID: Mbpp/748

# Description/Response:
"""
Write a function to put spaces between words starting with capital letters in a given string.
assert capital_words_spaces("Python") == 'Python'
"""
def capital_words_spaces(string):
    words = string.split()
    for i in range(len(words)):
        if words[i][0].isupper():
            words[i] = ' ' + words[i]
    return ''.join(words)