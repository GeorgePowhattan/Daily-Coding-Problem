'''You are given an array of integers. Find the maximum sum of all possible contiguous subarrays of the array.

Example:

[34, -50, 42, 14, -5, 86]

Given this input array, the output should be 137. The contiguous subarray with the largest sum is [42, 14, -5, 86].'''

def maxSequence(arr):
    if all(element < 0 for element in arr):
        return 0
    else:
        current_max = 0
        for i in range(len(arr)):
            for j in range(i,len(arr)+1):
               current_max = max(current_max, sum(arr[i:j]))
        return(current_max)
