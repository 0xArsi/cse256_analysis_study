# Task ID: Mbpp/459

# Description/Response:
"""
Write a function to remove uppercase substrings from a given string.
assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'
"""
def remove_uppercase(s):
    return ''.join([c for c in s if c.islower() or c.isdigit()])