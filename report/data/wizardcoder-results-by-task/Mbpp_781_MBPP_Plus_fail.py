# Task ID: Mbpp/781

# Description/Response:
"""
Write a python function to check whether the count of divisors is even. 
assert count_divisors(10)
"""
def count_divisors(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    if count % 2 == 0:
        return True
    else:
        return False