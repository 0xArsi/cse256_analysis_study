# Task ID: Mbpp/255

# Description/Response:
"""
Write a function that takes in a list and length n, and generates all combinations (with repetition) of the elements of the list and returns a list with a tuple for each combination.
assert combinations_colors( ["Red","Green","Blue"],1)==[('Red',), ('Green',), ('Blue',)]
"""
def combinations_colors(colors, n):
    if n == 1:
        return [(color,) for color in colors]
    else:
        return [(color,) + combination for color in colors for combination in combinations_colors(colors, n-1)]