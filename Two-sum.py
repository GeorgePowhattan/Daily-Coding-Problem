# You are given a list of numbers, and a target number k. Return whether or not there are two numbers in the list that add up to k.
lst = [4, 7, 1 , -3, 2]
k = 5

def two_sum(lst, k):
    length = len(lst)
    result = []
    for i in range(length):
        for j in range(i+1, length):
            if lst[i] + lst[j] == k:
                return True
    return False

two_sum(lst, k)