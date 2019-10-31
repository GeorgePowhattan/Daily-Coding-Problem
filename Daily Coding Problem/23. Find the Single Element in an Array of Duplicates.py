# Given an array of integers, arr, where all numbers occur twice except one number which occurs once, find the number. Your solution should ideally be O(n) time and use constant extra space.

'''Example:
Input: arr = [7, 3, 5, 5, 4, 3, 4, 8, 8]
Output: 7'''

def findSingle(nums):
    res = []
    for number in nums:
        if number not in res:
            res.append(number)
        else:
            res.remove(number)           
    return res

arr = [7, 3, 5, 5, 4, 3, 4, 8, 8]

print(findSingle(arr))


# Solution using hastable:

from collections import defaultdict

def findSingle_hash(nums):
    hashtable = defaultdict(int)
    for number in nums:
        hashtable[number] += 1
    return [count for count in hashtable if hashtable[count] == 1]
    
print(findSingle_hash(arr))
