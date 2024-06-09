# Task ID: Mbpp/428

# Description/Response:
"""
Write a function to sort the given array by using shell sort.
assert shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]) == [2, 3, 4, 5, 12, 12, 23, 56, 81, 95]
"""
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap):
            for j in range(i, n):
                temp = arr[j]
                k = j
                while k >= gap and arr[k - gap] > temp:
                    arr[k] = arr[k - gap]
                    k -= gap
                arr[k] = temp
        gap //= 2
    return arr