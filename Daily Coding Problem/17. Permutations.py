# You are given an array of integers. Return all the permutations of this array.

import itertools

def permute(nums):
    return [lst for lst in itertools.permutations(nums)]

lst = [1, 2, 3]

print(permute(lst))
# [[1, 2, 3], [2, 1, 3], [2, 3, 1], [1, 3, 2], [3, 1, 2], [3, 2, 1]]


# ------------------------------------------------------------------------------
# Permutations without itertools - recursion

def permute_rec(nums):
    if (len(nums) == 1):
        return [nums]

    output = []
    for l in permute_rec(nums[1:]):
        for idx in range(len(nums)):
            output.append(l[:idx] + [nums[0]] + l[idx:])
    return output


print(permute_rec([1, 2, 3]))