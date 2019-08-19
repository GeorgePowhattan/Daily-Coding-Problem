'''You 2 integers n and m representing an n by m grid, determine the number of ways you can get from the top-left to the bottom-right of the matrix y going only right or down.

Example:
n = 2, m = 2

This should return 2, since the only possible routes are:
Right, down
Down, right.'''

import math

def num_ways(n, m):
    comb = (math.factorial(n+m-2) / (math.factorial(m-1) * math.factorial(n-1)))
    return int(comb)

print(num_ways(2, 2))
# 2

