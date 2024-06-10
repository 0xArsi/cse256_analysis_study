# Task ID: Mbpp/576

# Description/Response:
"""
Write a python function to check whether a list is sublist of another or not.
assert is_Sub_Array([1,4,3,5],[1,2]) == False
"""
def is_Sub_Array(sub_list, main_list):
    if len(sub_list) > len(main_list):
        return False
    for i in range(len(main_list) - len(sub_list) + 1):
        if sub_list == main_list[i:i+len(sub_list)]:
            return True
    return False