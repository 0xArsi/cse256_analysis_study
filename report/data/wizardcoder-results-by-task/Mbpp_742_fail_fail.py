# Task ID: Mbpp/742

# Description/Response:
"""
Write a function to caluclate the area of a tetrahedron.
assert area_tetrahedron(3)==15.588457268119894
"""
def area_tetrahedron(a, b, c, d):
    """
    Calculates the area of a tetrahedron with side lengths a, b, c, and d.
    Returns the area of the tetrahedron.
    """
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area