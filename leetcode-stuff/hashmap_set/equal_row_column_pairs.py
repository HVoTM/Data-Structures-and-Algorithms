# LEETCODE 2352. Equal Row and Column Pairs
from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # Intuition:
        # We will check each column with each row? O(N^2)

        # initialize the count for the pair of equal row-column
        count = 0
        for i in range(len(grid)):
            # Get the i-th column of matrix using list comprehension 
            # we get each row and retrieve the corresponding element to that column ith index
            col = [sub[i] for sub in grid]

            # Now we compare with each row
            for j in range(len(grid)):
                if col == grid[j]:
                    count += 1
            
        return count


    # Let's cross-reference with the other solutions on the internet
    def AlgoMonster(self, grid: List[List[int]]) -> int:
        # Transpose the input grid to get columns as rows
        transposed_grid = [list(column) for column in zip(*grid)]
      
        # Initialize a counter for equal pairs
        equal_pairs_count = 0
      
        # Iterate through each row in the original grid
        for row in grid:
            # For each row, compare it with each row in the transposed grid (which are originally columns)
            for transposed_row in transposed_grid:
                # If the original row and the transposed row (column) match, increment the counter
                if row == transposed_row:
                    equal_pairs_count += 1
      
        # Return the total count of equal row-column pairs
        return equal_pairs_count

mat = [[3,2,1],[1,7,6],[2,7,7]]

solution = Solution()

print(solution.AlgoMonster(grid = mat)) 
