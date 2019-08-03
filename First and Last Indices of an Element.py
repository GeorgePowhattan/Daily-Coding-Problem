# Given a sorted array, A, with possibly duplicated elements, find the indices of the first and last occurrences of a target element, x. Return -1 if the target is not found.

# Define the array and the target element
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8, 9, 9, 9] 
x = 9

class Solution: 
    def getRange(self, arr, target):
        lst = []
        # 1. Return a list of indices of target number occurences in an arr
        for i, number in enumerate(arr):
            if number == target:
                lst.append(i)
        # 2. return "-1", single index or start/end index depeding on how many number occurences aare found
        if len(lst) == 0:
            return -1
        elif len(lst) == 1:
            return lst
        else:
            return ([lst[0],lst[-1]])

print(Solution().getRange(arr, x))
# [1, 4]