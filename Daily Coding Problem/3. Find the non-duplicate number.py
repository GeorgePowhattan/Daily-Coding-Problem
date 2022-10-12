# Given a list of numbers, where every number shows up twice except for one number, find that one number.

'''Example:
Input: [4, 3, 2, 4, 1, 3, 2]
Output: 1'''

# Solution:
def singleNumber(nums):
    result = []
    for number in nums:
        if nums.count(number) == 1:
            result.append(number)
    return result


lst = [4, 3, 2, 4, 1, 3, 2, 4]

print(singleNumber(lst))
