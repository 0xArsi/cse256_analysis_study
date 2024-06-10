# Task ID: Mbpp/455

# Description/Response:
"""
Write a function to check whether the given month number contains 31 days or not.
assert check_monthnumb_number(5)==True
"""
def check_monthnumb_number(month_num):
    """
    This function takes a month number as input and returns True if the given month has 31 days, else False.
    """
    if month_num in [1, 3, 5, 7, 8, 10, 12]:
        return True
    elif month_num in [4, 6, 9, 11]:
        return False
    elif month_num == 2:
        return True
    else:
        return False