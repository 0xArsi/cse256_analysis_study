# Task ID: Mbpp/745

# Description/Response:
"""
Write a function to find numbers within a given range from startnum ti endnum where every number is divisible by every digit it contains. 
assert divisible_by_digits(1,22)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
"""
def divisible_by_digits(startnum, endnum):
    result = []
    for num in range(startnum, endnum+1):
        if all(num%int(digit)==0 for digit in str(num)):
            result.append(num)
    return result