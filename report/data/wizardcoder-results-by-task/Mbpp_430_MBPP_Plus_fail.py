# Task ID: Mbpp/430

# Description/Response:
"""
Write a function to find the directrix of a parabola.
assert parabola_directrix(5,3,2)==-198
"""
def parabola_directrix(a, x, y_intercept):
    x_intercept = 1/a
    y_intercept = 1/a
    slope = -1/a
    return slope, x_intercept, y_intercept