# Task ID: Mbpp/730

# Description/Response:
"""
Write a function to remove consecutive duplicates of a given list.
assert consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
"""
def remove_consecutive_duplicates(lst):
    result = []
    for i in range(len(lst)):
        if i == 0 or lst[i] != lst[i-1]:
            result.append(lst[i])
    return result