# Task ID: Mbpp/735

# Description/Response:
"""
Write a python function to toggle bits of the number except the first and the last bit. 
assert toggle_middle_bits(9) == 15
"""
def toggle_middle_bits(n):
    # Convert the number to binary and get the length of the binary representation
    binary = bin(n)[2:]
    length = len(binary)
    
    # Toggle the bits of the number except the first and last bit
    for i in range(1, length-1):
        n ^= 1 << (length-2-i)
    
    # Return the modified number
    return n