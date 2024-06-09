# Task ID: Mbpp/392

# Description/Response:
"""
Write a function to find the maximum sum possible by using the given equation f(n) = max( (f(n/2) + f(n/3) + f(n/4) + f(n/5)), n).
assert get_max_sum(60) == 106
"""
def get_max_sum(n):
    def helper(n):
        if n == 1:
            return 0
        elif n % 15 == 0:
            return n // 15
        elif n % 5 == 0:
            return n // 5 + helper(n // 5)
        elif n % 4 == 0:
            return n // 4 + helper(n // 4)
        elif n % 3 == 0:
            return n // 3 + helper(n // 3)
        elif n % 2 == 0:
            return n // 2 + helper(n // 2)
        else:
            return n
    
    return max(helper(n), helper(n/2) + helper(n/3) + helper(n/4) + helper(n/5))