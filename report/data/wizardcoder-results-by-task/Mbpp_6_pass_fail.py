# Task ID: Mbpp/6

# Description/Response:
"""
Write a python function to check whether the two numbers differ at one bit position only or not.
assert differ_At_One_Bit_Pos(13,9) == True
"""
def differ_At_One_Bit_Pos(num1, num2):
    # Convert the numbers to binary strings
    bin1 = bin(num1)[2:].zfill(8)
    bin2 = bin(num2)[2:].zfill(8)
    
    # Iterate through the binary strings and count the number of differences
    count = 0
    for i in range(len(bin1)):
        if bin1[i] != bin2[i]:
            count += 1
            if count > 1:
                return False
    
    # If there is only one difference, return True, else False
    return count == 1