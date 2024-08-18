#!/usr/bin/env python3
# A function to find a peak in array.

def findPeak(L):
    """Find peaks in the array

    Args:
        L (list): The list containing all elements

    Returns:
        List: A list containing peak elements. 
    """
    results = []
    for i in range(1, len(L) - 1):
        if L[i] > L[i-1] and L[i] > L[i+1]:
            results.append(L[i])
    if L[0] > L[1]: results.append(L[0])
    if L[-1] > L[-2]: results.append(L[-1])
    return results
array = [3,2,4,5,4,3,1,2,2]
print("The peak points are: ", findPeak(array))
