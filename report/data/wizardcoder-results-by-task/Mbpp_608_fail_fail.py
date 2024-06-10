# Task ID: Mbpp/608

# Description/Response:
"""
Write a python function to find nth bell number.
assert bell_Number(2) == 2
"""
def bell_Number(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        bell = [1, 2]
        for i in range(2, n):
            bell.append(bell[i-1] + bell[i-2])
        return bell[n-1]