# Task ID: Mbpp/626

# Description/Response:
"""
Write a python function to find the area of the largest triangle that can be inscribed in a semicircle with a given radius.
assert triangle_area(-1) == None
"""
import math

def triangle_area(radius):
    if radius < 0:
        return None
    else:
        area = math.pi * radius**2 / 2
        return area