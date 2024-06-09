# Task ID: Mbpp/131

# Description/Response:
"""
Write a python function to reverse only the vowels of a given string (where y is not a vowel).
assert reverse_vowels("Python") == "Python"
"""
def reverse_vowels(s):
    vowels = "aeiouAEIOU"
    vowels_reversed = ""
    non_vowels = ""
    for char in s:
        if char in vowels:
            vowels_reversed = char + vowels_reversed
        else:
            non_vowels = char + non_vowels
    return non_vowels + vowels_reversed