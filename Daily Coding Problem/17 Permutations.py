# You are given an array of integers. Return all the permutations of this array.

import itertools

def permute(nums):
    return [lst for lst in itertools.permutations(nums)]

lst = [1, 2, 3]

print(permute(lst))
# [[1, 2, 3], [2, 1, 3], [2, 3, 1], [1, 3, 2], [3, 1, 2], [3, 2, 1]]


# ------------------------------------------------------------------------------
# without itertools - recursion?

