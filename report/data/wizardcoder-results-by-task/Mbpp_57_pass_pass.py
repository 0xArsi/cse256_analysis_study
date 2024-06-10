# Task ID: Mbpp/57

# Description/Response:
"""
Write a python function to find the largest number that can be formed with the given list of digits.
assert find_Max_Num([1,2,3]) == 321
"""
def find_Max_Num(digits):
    digits.sort(reverse=True)
    result = 0
    for digit in digits:
        result = result * 10 + digit
    return result