# Task ID: Mbpp/739

# Description/Response:
"""
Write a python function to find the index of smallest triangular number with n digits. 
assert find_Index(2) == 4
"""
def find_Index(n):
    i = 1
    while True:
        if len(str(i*(i+1)//2)) == n:
            return i
        i += 1