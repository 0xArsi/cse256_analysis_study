# Task ID: Mbpp/74

# Description/Response:
"""
Write a function to check whether it follows the sequence given in the patterns array.
assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True
"""
def is_samepatterns(patterns, lst):
    if len(patterns) != len(lst):
        return False
    
    for i in range(len(patterns)):
        if patterns[i] == lst[i]:
            continue
        elif patterns[i] in lst[i]:
            return False
        elif lst[i] in patterns[i]:
            return False
        else:
            return False
    
    return True