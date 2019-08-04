# Given a sorted array, A, with possibly duplicated elements, find the indices of the first and last occurrences of a target element, x. Return -1 if the target is not found.

class Solution: 
    def getRange(self, arr, target):
        lst = []
        # 1. Return a list of indices of Target Element occurences in an array
        for i, number in enumerate(arr):
            if number == target:
                lst.append(i)
        # 2. return "-1", single index or start/end index depeding on how many Target Element occurences are found
        if len(lst) == 0:
            return -1
        elif len(lst) == 1:
            return lst
        else:
            return ([lst[0],lst[-1]])

# Define the array and the Target Element
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8, 9, 9, 9] 
x = 9

print(Solution().getRange(arr, x))