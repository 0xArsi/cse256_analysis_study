# Task ID: Mbpp/109

# Description/Response:
"""
Write a python function to find the number of numbers with an odd value when rotating a binary string the given number of times.
assert odd_Equivalent("011001",6) == 3
"""
def odd_Equivalent(binary_string, rotations):
    binary_string = list(binary_string)
    for i in range(rotations):
        last_digit = binary_string.pop()
        binary_string.insert(0, last_digit)
    
    count = 0
    for digit in binary_string:
        if int(digit) % 2 == 1:
            count += 1
    
    return count