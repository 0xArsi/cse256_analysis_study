# Task ID: Mbpp/305

# Description/Response:
"""
Write a function to return two words from a list of words starting with letter 'p'.
assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
"""
def start_withp(words):
    p_words = []
    for word in words:
        if word.startswith('p'):
            p_words.append(word)
    return tuple(p_words[:2])