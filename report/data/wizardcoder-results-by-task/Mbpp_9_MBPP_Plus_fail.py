# Task ID: Mbpp/9

# Description/Response:
"""
Write a python function to find the minimum number of rotations (greater than 0) required to get the same string.
assert find_Rotations("aaaa") == 1
"""
def find_Rotations(s):
    n = len(s)
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        if s[0] == s[1]:
            return 0
        else:
            return 1
    else:
        for i in range(n):
            if s[i] == s[0]:
                return i
        return n