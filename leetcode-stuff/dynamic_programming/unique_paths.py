# LeetCode 62. Unique Paths
from functools import lru_cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """Bruh, literal cheatcode using lru_cache so you do not need
        to initialize a way to keep track for redundant moves"""
        @lru_cache(None)  # Use lru_cache for memoization to improve performance

        def count_ways(row: int, col: int) -> int:
            # base case
            if row > n-1 or col > m-1:
                return 0
            # if reached end point
            if row == n-1 and col == m-1:
                return 1

            # Initialize the possily unique paths that the robot can take to reach the bottom-right corner
            ways = 0

            # The robot can only move down or right so
            ways += count_ways(row+1, col)
            ways += count_ways(row, col+1)
            return ways
        
        return count_ways(0, 0)
    
    def NeetCode(self, m:int, n:int) -> int:
        #https://www.youtube.com/watch?v=IlEsdxuD4lY&ab_channel=NeetCode
        row = [1] * n

        for i in range(m-1):
            newRow = [1] * n
            for j in range(n-2, -1, -1):
                newRow[j] = newRow[j+1] + row[j]

            row = newRow
        return row[0]