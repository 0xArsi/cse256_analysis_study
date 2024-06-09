# Task ID: Mbpp/123

# Description/Response:
"""
Write a function to sum all amicable numbers from 1 to a specified number.
assert amicable_numbers_sum(999)==504
"""
def amicable_numbers_sum(n):
    def is_amicable(num):
        sum_divisors = sum(d for d in range(1, num) if num % d == 0)
        return sum_divisors == num

    def sum_divisors(num):
        return sum(d for d in range(1, num) if num % d == 0)

    total = 0
    for i in range(1, n+1):
        if is_amicable(i) and is_amicable(sum_divisors(i)):
            total += i
    return total