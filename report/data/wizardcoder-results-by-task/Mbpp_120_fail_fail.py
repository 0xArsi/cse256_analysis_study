# Task ID: Mbpp/120

# Description/Response:
"""
Write a function to find the maximum absolute product between numbers in pairs of tuples within a given list.
assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==36
"""
def max_product_tuple(lst):
    max_product = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            product = lst[i][0] * lst[j][1]
            if product > max_product:
                max_product = product
    return max_product