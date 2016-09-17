# Complete the function below.
# Given an array of positive integers
# Return the number of subarrays with product
# less than an integer k
import math
def  count(numbers, k):
    n = len(numbers)
    maxProductSub = 0
    prod = 1
    left = 0
    right = -1
    for left in range(n):
        while(right + 1 < n and numbers[right + 1] < math.ceil(k / prod)):
            right += 1
            prod *= numbers[right]

        subArraySize = right - left + 1
        maxProductSub += subArraySize
        
        prod /= numbers[left]
    return maxProductSub
   