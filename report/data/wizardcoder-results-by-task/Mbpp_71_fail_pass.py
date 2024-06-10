# Task ID: Mbpp/71

# Description/Response:
"""
Write a function to sort a list of elements.
assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
"""
def comb_sort(arr):
    n = len(arr)
    gap = n
    sorted = False
    while not sorted:
        gap = max(1, int(gap / 1.3))
        sorted = True
        for i in range(n - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted = False
        if gap > 1:
            for i in range(n - gap - 1):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    sorted = False
    return arr