'''Given a 2d n x m matrix where each cell has a certain amount of change on the floor, your goal is to start from the top left corner mat[0][0] and end in the bottom right corner mat[n - 1][m - 1] with the most amount of change. You can only move either left or down.'''

def max_change(mat):
    if len(mat) == 1:
        return sum([number for sublist in mat for number in sublist])
    if len(mat[0]) == 1:
        return sum([lst[0] for lst in mat])
    # recursive solution: the max path collected is equal to the larger of the UP or LEFT max path, until the matrix of len(1) is reached.
    return max(max_change(mat[:][:-1]), max_change([lst[:-1] for lst in mat]) ) + mat[-1][-1]
    
mat = [
    [0, 3, 0, 2],
    [1, 2, 3, 3],
    [6, 0, 3, 2]
]

print(max_change(mat))
# 13
