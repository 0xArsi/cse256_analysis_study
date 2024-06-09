# Task ID: Mbpp/260

# Description/Response:
"""
Write a function to find the nth newman–shanks–williams prime number.
assert newman_prime(3) == 7
"""
def newman_prime(n):
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        count = 0
        num = 5
        while count < n:
            num += 2
            if is_prime(num):
                count += 1
        return num

def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        for i in range(3, int(num**0.5)+1, 2):
            if num % i == 0:
                return False
        return True