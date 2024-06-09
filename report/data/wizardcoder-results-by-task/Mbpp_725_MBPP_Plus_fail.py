# Task ID: Mbpp/725

# Description/Response:
"""
Write a function to extract values between quotation marks " " of the given string.
assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']
"""
def extract_quotation(s):
    return [x[1:-1] for x in s.split('"') if x.isalnum()]