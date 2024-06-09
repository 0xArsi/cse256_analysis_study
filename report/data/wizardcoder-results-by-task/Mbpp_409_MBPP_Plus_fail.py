# Task ID: Mbpp/409

# Description/Response:
"""
Write a function to find the minimum product from the pairs of tuples within a given list.
assert min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==8
"""
def min_product_tuple(lst):
    """
    Given a list of tuples, find the minimum product of any two tuples in the list.
    """
    min_product = float('inf')
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            product = lst[i][0] * lst[j][1]
            if product < min_product:
                min_product = product
    return min_product