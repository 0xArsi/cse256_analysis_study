# Task ID: Mbpp/771

# Description/Response:
"""
Write a function to check if the given expression is balanced or not. 
assert check_expression("{()}[{}]") == True
"""
def check_expression(expr):
    stack = []
    for char in expr:
        if char in ["(", "{", "["]:
            stack.append(char)
        elif char in [")", "}", "]"]:
            if not stack:
                return False
            if (char == ")" and stack[-1] == "(") or (char == "]" and stack[-1] == "{"):
                stack.pop()
            else:
                return False
    return not stack