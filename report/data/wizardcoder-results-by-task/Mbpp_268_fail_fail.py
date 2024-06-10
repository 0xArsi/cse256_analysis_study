# Task ID: Mbpp/268

# Description/Response:
"""
Write a function to find the n'th star number.
assert find_star_num(3) == 37
"""
def find_star_num(n):
    """
    Returns the n'th star number.
    """
    if n < 1:
        return None
    elif n == 1:
        return 1
    else:
        return 1 + 4 * (n - 1) + find_star_num(n - 1)