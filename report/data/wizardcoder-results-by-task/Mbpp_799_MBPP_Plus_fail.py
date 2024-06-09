# Task ID: Mbpp/799

# Description/Response:
"""
Write a function to that rotate left bits by d bits a given number. We assume that the number is 32 bit.
assert left_rotate(16,2) == 64
"""
def left_rotate(num, d):
    # Convert the number to binary and get the length of the binary string
    binary_num = bin(num)[2:]
    length = len(binary_num)
    
    # Calculate the number of bits to be rotated
    rotate_bits = d % length
    
    # Rotate the bits to the left
    rotated_num = num << rotate_bits
    
    # Shift the bits to the right by length - rotate_bits
    rotated_num |= num >> (length - rotate_bits)
    
    # Convert the rotated binary number back to decimal and return it
    return int(rotated_num)