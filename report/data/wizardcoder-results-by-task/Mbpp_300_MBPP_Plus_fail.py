# Task ID: Mbpp/300

# Description/Response:
"""
Write a function to find the count of all binary sequences of length 2n such that sum of first n bits is same as sum of last n bits.
assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
"""
def count_binary_seq(n):
    # Initialize the count variable
    count = 0
    # Loop through all possible binary sequences of length 2n
    for i in range(2**(2*n):
        # Convert the binary sequence to a list of bits
        bits = list(format(i, f'0{2*n}b'))
        # Check if the sum of the first n bits is equal to the sum of the last n bits
        if sum(bits[:n]) == sum(bits[n:]):
            count += 1
    # Return the count
    return count