# Task ID: Mbpp/784

# Description/Response:
"""
Write a function to find the product of first even and odd number of a given list.
assert mul_even_odd([1,3,5,7,4,1,6,8])==4
"""
def mul_even_odd(lst):
    even_product = 1
    odd_product = 1
    even_count = 0
    odd_count = 0
    for num in lst:
        if num % 2 == 0:
            even_product *= num
            even_count += 1
        else:
            odd_product *= num
            odd_count += 1
        if even_count > 0 and odd_count > 0:
            break
    return even_product * odd_product