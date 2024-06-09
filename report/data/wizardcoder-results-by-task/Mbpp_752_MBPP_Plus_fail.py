# Task ID: Mbpp/752

# Description/Response:
"""
Write a function to find the nth jacobsthal number.  0, 1, 1, 3, 5, 11, 21, 43, 85, 171, 341, 683, 1365, 2731, ...
assert jacobsthal_num(5) == 11
"""
def jacobsthal_num(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return 2 * jacobsthal_num(n-1)**2 - jacobsthal_num(n-2)