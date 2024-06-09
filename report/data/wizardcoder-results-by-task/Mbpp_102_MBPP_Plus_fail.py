# Task ID: Mbpp/102

# Description/Response:
"""
Write a function to convert a snake case string to camel case string.
assert snake_to_camel('python_program')=='PythonProgram'
"""
def snake_to_camel(snake_str):
    words = snake_str.split('_')
    return words[0].lower() + ''.join(word.title() for word in words[1:])