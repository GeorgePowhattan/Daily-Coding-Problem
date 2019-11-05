'''You are given an array of integers. Find the maximum sum of all possible contiguous subarrays of the array.

Example:

[34, -50, 42, 14, -5, 86]

Given this input array, the output should be 137. The contiguous subarray with the largest sum is [42, 14, -5, 86].'''

# Brute force solution
def max_subarray_sum(arr):
    sum_arr = []
    if all(element < 0 for element in arr):
        return 0
    for i in range(len(a)):
        for j in range (i+1, len(a)+1):
            sum_arr.append(sum(a[i:j]))
    return max(sum_arr)

# Better solution running in linear time:
def max_subarray_sum_linear(arr):
    if all(element < 0 for element in arr):
        return 0
    max_sum_arr = 0
    sum_arr = 0
    for number in arr:
        if number >= 0:
            sum_arr += number
            max_sum_arr = max(max_sum_arr, sum_arr)
        else:
            sum_arr += number
            sum_arr = max(0, sum_arr) 
    return max_sum_arr
    
b = [random.randint(-5,10) for i in range(0,10)]
c = [random.randint(-5,10) for i in range(0,10)]
d = [random.randint(-5,10) for i in range(0,10)]
print(b)
print(c)
print(d)

# Test both solutions: 
print(max_subarray_sum(b))
print(max_subarray_sum(c))
print(max_subarray_sum(d))
print(max_subarray_sum_linear(b))
print(max_subarray_sum_linear(c))
print(max_subarray_sum_linear(d))
