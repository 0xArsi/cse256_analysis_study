# Task ID: Mbpp/637

# Description/Response:
"""
Write a function to check whether the given amount has no profit and no loss
assert noprofit_noloss(1500,1200)==False
"""
def noprofit_noloss(amount1, amount2):
    if amount1 == amount2:
        return True
    elif amount1 > amount2:
        return False
    else:
        return True