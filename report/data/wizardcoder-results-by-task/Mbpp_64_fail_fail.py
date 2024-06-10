# Task ID: Mbpp/64

# Description/Response:
"""
Write a function to sort a list of tuples using the second value of each tuple.
assert subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])==[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
"""
def sort_by_second(tuples_list):
    return sorted(tuples_list, key=lambda x: x[1])