# Task ID: Mbpp/252

# Description/Response:
"""
Write a python function to convert complex numbers to polar coordinates.
assert convert(1) == (1.0, 0.0)
"""
def convert(z):
    r = abs(z)
    theta = math.atan2(z.imag, z.real)
    return (r, theta)