# Task ID: Mbpp/618

# Description/Response:
"""
Write a function to divide two lists element wise.
assert div_list([4,5,6],[1, 2, 3])==[4.0,2.5,2.0]
"""
def div_list(list1, list2):
    result = []
    for i in range(len(list1)):
        result.append(list1[i]/list2[i])
    return result