# Task ID: Mbpp/61

# Description/Response:
"""
Write a python function to count the number of substrings with the sum of digits equal to their length.
assert count_Substrings('112112') == 6
"""
def count_Substrings(s):
    count = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if sum(int(d) for d in s[i:j+1]) == j-i+1:
                count += 1
    return count