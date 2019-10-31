'''Longest Consecutive SequenceYou are given an array of integers.

Return the length of the longest consecutive elements sequence in the array.

For example, the input array [100, 4, 200, 1, 3, 2] has the longest consecutive sequence 1, 2, 3, 4, and thus, you should return its length, 4.'''


def longest_consecutive(nums):
    nums_sorted = sorted(nums)
    cons = 1
    max_cons = 1
    for i in range(1, len(nums)):
        if nums_sorted[i] == nums_sorted[i-1] + 1:
            cons += 1
            max_cons = max(max_cons, cons)
        else:
            cons = 1
    return max_cons
    
a = [100, 4, 200, 1, 3, 2, 101, 102, 103, 104]

print(longest_consecutive(a))

