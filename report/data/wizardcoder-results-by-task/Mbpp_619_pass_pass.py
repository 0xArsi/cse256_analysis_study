# Task ID: Mbpp/619

# Description/Response:
"""
Write a function to move all the numbers to the end of the given string.
assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
"""
def move_num(string):
    nums = []
    non_nums = []
    for char in string:
        if char.isdigit():
            nums.append(char)
        else:
            non_nums.append(char)
    return ''.join(non_nums) + ''.join(nums)