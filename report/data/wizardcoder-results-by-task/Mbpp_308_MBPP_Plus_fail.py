# Task ID: Mbpp/308

# Description/Response:
"""
Write a function to find the specified number of largest products from two given lists, selecting one factor from each list.
assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]
"""
def large_product(list1, list2, n):
    # Sort both lists in descending order
    list1.sort(reverse=True)
    list2.sort(reverse=True)
    
    # Initialize an empty list to store the largest products
    largest_products = []
    
    # Iterate over the first n elements of both lists and append the product to the list
    for i in range(n):
        largest_products.append(list1[i] * list2[i])
    
    # Return the list of largest products
    return largest_products