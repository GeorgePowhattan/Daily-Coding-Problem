'''Given an array of integers of size n, where all elements are between 1 and n inclusive, find all of the elements of [1, n] that do not appear in the array. Some numbers may appear more than once.

Example:
Input: [4,5,2,6,8,2,1,5]
Output: [3,7]'''

def findDisappearedNumbers(nums):
    sort_nums = sorted(nums)
    res = []
    for i in range(1, len(sort_nums)):
        diff = sort_nums[i] - sort_nums[i-1]
        if diff == 1 or diff == 0:
            continue
        else:
            miss = sort_nums[i-1]
            for j in range(1, diff):
                miss += 1
                res.append(miss)
    return res

nums = [4, 6, 2, 6, 7, 2, 1]

print(findDisappearedNumbers(nums))