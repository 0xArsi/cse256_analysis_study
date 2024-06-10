# Task ID: Mbpp/99

# Description/Response:
"""
Write a function to convert the given decimal number to its binary equivalent, represented as a string with no leading zeros.
assert decimal_to_binary(8) == '1000'
"""
def decimal_to_binary(num):
    binary = ""
    while num > 0:
        binary = str(num % 2) + binary
        num = num // 2
    return binary if binary else "0"