# Task ID: Mbpp/643

# Description/Response:
"""
Write a function that checks if a strings contains 'z', except at the start and end of the word.
assert text_match_wordz_middle("pythonzabc.")==True
"""
def text_match_wordz_middle(text):
    return 'z' in text[1:-1]