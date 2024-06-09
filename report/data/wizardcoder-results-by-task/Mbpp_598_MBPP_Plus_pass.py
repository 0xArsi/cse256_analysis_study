# Task ID: Mbpp/598

# Description/Response:
"""
Write a function to check whether the given number is armstrong or not.
assert armstrong_number(153)==True
"""
def armstrong_number(num):
    # convert the number to string
    num_str = str(num)
    # get the length of the number
    length = len(num_str)
    # initialize sum to zero
    sum = 0
    # iterate through each digit of the number
    for digit in num_str:
        # add the cube of the digit to the sum
        sum += int(digit) ** length
    # if the sum is equal to the original number, return True
    if sum == num:
        return True
    else:
        return False