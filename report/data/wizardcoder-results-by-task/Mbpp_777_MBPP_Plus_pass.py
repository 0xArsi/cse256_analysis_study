# Task ID: Mbpp/777

# Description/Response:
"""
Write a python function to find the sum of non-repeated elements in a given list.
assert find_sum([1,2,3,1,1,4,5,6]) == 21
"""
def find_sum(lst):
    seen = set()
    total = 0
    for num in lst:
        if num not in seen:
            seen.add(num)
            total += num
    return total