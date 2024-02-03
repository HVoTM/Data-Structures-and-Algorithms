"""
GRID TRAVELING PROBLEM
Given the value units of a 2-dimension grid, you begin in the top-left corner and are only able to move down or right.

Compute on how many ways to travel the m * n grids to the bottom-right corner as the goal.
"""
# recursive function
def rec_gridtraveler(m, n):
    # Base case:
    if (m == 1) & (n == 1):
        return 1
    if (m == 0) | (n == 0):
        return 0
    return rec_gridtraveler(m - 1, n) + rec_gridtraveler(m, n - 1)

# Top-down method (Memoization):
def topdown_gridtraveler(m, n, memo={}):
    # first, let's save the key to the memo for options to work with
    key = str(m) + ',' + str(n)
    if key in memo:
        return memo[key]
    
    # Base case of [1, 1] and [0,_] or [_, 0]
    if (m == 1) & (n == 1):
        return 1
    if (m == 0) | (n == 0):
        return 0
    
    # save the solution to the sub-problem to the memo
    memo[key] = topdown_gridtraveler(m - 1, n, memo) + topdown_gridtraveler(m, n - 1, memo) # pass down memo to share with 
                                                                                            # the rest of the recursive calls
    return memo[key] 
"""
Big-O complexity
Time complexity: O(m * n)
Space complexity: O(n + m)
"""
import numpy as np
# Bottom-up method (Tabulation)
def bottomup_gridtraveler(m, n):
    # Create a 2D-array with dimensions (m + 1) * (n + 1) to make up the matrix
    table = np.zeros((m+1, n+1))
    table[0, 0] = 1

    for i in range(m + 1):
        for j in range(n + 1):
            current = table[i, j]
            if (j + 1) <= n: # Check if the pointer goes out of bound
                table[i, j + 1] += current
            if (i + 1) <= m:
                table[i + 1, j] += current
    print(table)
    return int(table[m - 1, n - 1])

print(rec_gridtraveler(10, 15))
print(topdown_gridtraveler(10 ,15))
print(bottomup_gridtraveler(4, 3))