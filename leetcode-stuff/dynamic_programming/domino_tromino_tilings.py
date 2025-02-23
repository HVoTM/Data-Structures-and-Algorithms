# LEETCODE 790. Domino and Tromino Tilings
# 2D Arrays, Dynamic Programming

from functools import lru_cache  # Import lru_cache for memoization

class Solution:
    def numTilings(self, n: int) -> int:
        # A helper function with memoization to count the number of ways to tile the board.
        # i represents the tiles placed in the first row, and j represents the tiles in the second row.
        @lru_cache(None)  # Use lru_cache for memoization to improve performance
        def count_ways(first_row: int, second_row: int) -> int:
            # Base case: If we exceed the board size, there's no way to tile.
            if first_row > n or second_row > n:
                return 0
            # Base case: If both rows are completely tiled, we've found one valid tiling.
            if first_row == n and second_row == n:
                return 1
          
            # Initialization of possible ways to tile.
            ways = 0 
            # When both rows have the same number of points covered by tiles.
            if first_row == second_row:
                ways = (
                    count_ways(first_row + 2, second_row + 2) +  # Place a 2x2 square.
                    count_ways(first_row + 1, second_row + 1) +  # Place two 2x1 tiles, one in each row.
                    count_ways(first_row + 2, second_row + 1) +  # Place a 'L' shaped tromino.
                    count_ways(first_row + 1, second_row + 2)    # Place an inverted 'L' shaped tromino.
                )
            elif first_row > second_row:
                # If the first row has more tiles than the second row.
                ways = count_ways(first_row, second_row + 2) + count_ways(first_row + 1, second_row + 2)
            else:
                # If the second row has more tiles than the first row.
                ways = count_ways(first_row + 2, second_row) + count_ways(first_row + 2, second_row + 1)

            # Return the ways modulo MOD, which represents the maximum number of unique tilings.
            return ways % MOD

        # Define the modulo constant to prevent large number arithmetic issues.
        MOD = 10**9 + 7
        # Call the helper function with the initial states of the board (0 tiles placed).
        return count_ways(0, 0)
    
MOD = 1000000007
dp = [[] * 4 for _ in range(n+1)]

def makeState(t1, t2):
    if not t1 and not t2: 
        return 0
    if t1 and not t2:
        return 1
    if not t1 and t2:
        return 2
    return 3

def f(i, t1, t2):
    if i == n:
        return 1
    state = makeState(t1, t2)

    if dp[i][state]:
        return dp[i][state]
    
    t3, t4 = i+1 <n, i+1<n

    count = 0 

    if (t1 and t2 and t3):
        count += f(i+1, False, True)
    if (t1 and t2 and t4):
        count += f(i+1, True, False)
    if (t1 and not t2 and t3 and t4):
        count += f(i+1, False, False)
    if (not t1 and t2 and t3 and t3):
        count += f(i+1, False, False)
    
    if (t1 and t2):
        count += f(i+1, True, True)
    if (t1 and t2 and t3 and t4):
        count += f(i+1, False, False)
    if (t1 and not t2 and t3):
        count += f(i+1, False, True)
    if (not t1 and t2 and t4):
        count += f(i+1, True, False)
    if (not t1 and not t2):
        count += f(i+1, True, True)

    dp[i][state] = count % MOD
    return dp[i][state]

return f(0, True, True)