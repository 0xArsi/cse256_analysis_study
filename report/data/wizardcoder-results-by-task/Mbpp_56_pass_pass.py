# Task ID: Mbpp/56

# Description/Response:
"""
Write a python function to check if a given number is one less than twice its reverse.
assert check(70) == False
"""
def check(num):
    return num == int(str(num)[::-1])*2-1