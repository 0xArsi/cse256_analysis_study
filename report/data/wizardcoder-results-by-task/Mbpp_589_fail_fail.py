# Task ID: Mbpp/589

# Description/Response:
"""
Write a function to find perfect squares between two given numbers.
assert perfect_squares(1,30)==[1, 4, 9, 16, 25]
"""
def perfect_squares(start, end):
    """
    Returns a list of all perfect squares between start and end (inclusive).
    """
    squares = []
    for i in range(start, end+1):
        if i**0.5 == int(i**0.5):
            squares.append(i**2)
    return squares