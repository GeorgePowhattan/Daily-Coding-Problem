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
        
    total = []
    for height, right, left in zip(arr, rightmax, list(reversed(leftmax))):
        total.append(max(0, min(right,left) - height))
    
    return sum(total)
