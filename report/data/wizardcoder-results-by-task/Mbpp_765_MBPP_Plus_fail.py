# Task ID: Mbpp/765

# Description/Response:
"""
Write a function to find nth polite number. geeksforgeeks.org/n-th-polite-number/
assert is_polite(7) == 11
"""
def is_polite(n):
    """
    Returns the nth polite number.
    """
    def polite_numbers():
        """
        Generates polite numbers.
        """
        i = 1
        while True:
            yield i
            i += 1

    def is_polite(num):
        """
        Checks if a number is polite.
        """
        for digit in str(num):
            if int(digit) % 2 == 0:
                return False
        return True

    count = 0
    for num in polite_numbers():
        if is_polite(num):
            count += 1
            if count == n:
                return num