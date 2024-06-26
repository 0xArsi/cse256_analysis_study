# Task ID: Mbpp/749

# Description/Response:
"""
Write a function to sort a given list of strings of numbers numerically. 
assert sort_numeric_strings( ['4','12','45','7','0','100','200','-12','-500'])==[-500, -12, 0, 4, 7, 12, 45, 100, 200]
"""
def sort_numeric_strings(lst):
    return sorted(lst, key=lambda x: int(x))