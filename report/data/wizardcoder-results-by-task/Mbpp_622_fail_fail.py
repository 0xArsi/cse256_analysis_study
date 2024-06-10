# Task ID: Mbpp/622

# Description/Response:
"""
Write a function to find the median of two sorted lists of same size.
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
"""
def get_median(list1, list2, size):
    """
    Returns the median of two sorted lists of same size.
    """
    # Initialize two pointers for each list
    i = j = 0
    
    # Initialize a counter for the number of elements processed
    count = 0
    
    # Initialize a variable to store the sum of the two middle elements
    mid_sum = 0
    
    # Loop through both lists until we reach the middle of the lists
    while count < size // 2:
        # If the current element in list1 is smaller than the current element in list2, increment i and move to the next element in list1
        if list1[i] < list2[j]:
            i += 1
        # If the current element in list2 is smaller than the current element in list1, increment j and move to the next element in list2
        elif list2[j] < list1[i]:
            j += 1
        # If the current element in both lists are equal, increment both pointers
        else:
            i += 1
            j += 1
        
        # Increment the count of processed elements
        count += 1
    
    # If the size of the lists is odd, return the middle element
    if size % 2 == 1:
        return (list1[i] + list2[j]) / 2
    
    # If the size of the lists is even, return the average of the middle two elements
    else:
        # If the current element in list1 is smaller than the current element in list2, increment i and move to the next element in list1
        if list1[i] < list2[j]:
            i += 1
        # If the current element in list2 is smaller than the current element in list1, increment j and move to the next element in list2
        elif list2[j] < list1[i]:
            j += 1
        
        # Add the middle two elements to the sum variable
        mid_sum += list1[i] + list2[j]
        
        # Return the average of the middle two elements
        return mid_sum / 2