# Task ID: Mbpp/11

# Description/Response:
"""
Write a python function to remove first and last occurrence of a given character from the string.
assert remove_Occ("hello","l") == "heo"
"""
def remove_Occ(string, char):
    first = string.find(char)
    last = string.rfind(char)
    if first == -1 or last == -1:
        return string
    elif first == 0 and last == len(string) - 1:
        return string[:-1]
    elif first == len(string) - 1:
        return string[:first]
    elif last == 0:
        return string[1:]
    else:
        return string[:first] + string[first+1:last] + string[last+1:]