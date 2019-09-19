'''You have a landscape, in which puddles can form. You are given an array of non-negative integers representing the elevation at each location. Return the amount of water that would accumulate if it rains.

For example: [0,1,0,2,1,0,1,3,2,1,2,1] should return 6 because 6 units of water can get trapped here.'''

def capacity(arr):
    rightmax = [0 for _ in range(len(arr))]
    leftmax = [0 for _ in range(len(arr))]
    highest = 0
    
    for i, number in enumerate(arr[:-1]):
        if number > highest:
            highest = number
        rightmax[i+1] = highest
    
    highest = 0
    for j, number in enumerate(arr[:0:-1]):
        if number > highest:
            highest = number
        leftmax[j+1] = highest
    
    # the amount of water that can be stored on a given index is equal to the smaller of the highest value to its left and the highest value to its right, minus the height at that index
    total = []
    for height, right, left in zip(arr, rightmax, list(reversed(leftmax))):
        total.append(max(0, min(right,left) - height))      
    
    return sum(total)

print(capacity([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
