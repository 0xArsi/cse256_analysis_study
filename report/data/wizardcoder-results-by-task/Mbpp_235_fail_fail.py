# Task ID: Mbpp/235

# Description/Response:
"""
Write a python function to set all even bits of a given number.
assert even_bit_set_number(10) == 10
"""
def even_bit_set_number(num):
    """
    This function takes a number as input and sets all even bits to 1.
    """
    # Convert the number to binary and remove the prefix '0b'
    binary_num = bin(num)[2:]
    # Iterate over each bit in the binary number and set the even bits to 1
    for i in range(len(binary_num)):
        if i % 2 == 0:
            binary_num = binary_num[:i] + '1' + binary_num[i+1:]
    # Convert the binary number back to decimal and return the result
    return int(binary_num, 2)