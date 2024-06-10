# Task ID: Mbpp/299

# Description/Response:
"""
Write a function to calculate the maximum aggregate from the list of tuples.
assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)
"""
def max_aggregate(lst):
    max_name = ''
    max_score = 0
    for name, score in lst:
        if score > max_score:
            max_name = name
            max_score = score
        elif score == max_score and name < max_name:
            max_name = name
    return (max_name, max_score)