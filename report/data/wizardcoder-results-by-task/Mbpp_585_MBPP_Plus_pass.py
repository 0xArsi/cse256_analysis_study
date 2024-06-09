# Task ID: Mbpp/585

# Description/Response:
"""
Write a function to find the n most expensive items in a given dataset.
assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)==[{'name': 'Item-2', 'price': 555.22}]
"""
def expensive_items(data, n):
    sorted_data = sorted(data, key=lambda x: x['price'], reverse=True)
    return sorted_data[:n]