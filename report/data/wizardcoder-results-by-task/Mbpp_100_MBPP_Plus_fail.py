# Task ID: Mbpp/100

# Description/Response:
"""
Write a function to find the next smallest palindrome of a specified integer, returned as an integer.
assert next_smallest_palindrome(99)==101
"""
def next_smallest_palindrome(n):
    if n % 10 == 0:
        return n + 1
    
    n += 1
    while not is_palindrome(n):
        n += 1
    
    return n

def is_palindrome(n):
    return str(n) == str(n)[::-1]