# LEETCODE 994. Rotting Oranges
# concepts: Breadth-first search traversal, timer  count, deque
from typing import List
from collections import deque

class Solution:
    # algomonster: https://algo.monster/liteproblems/994
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Get the number of rows and columns of the grid.
        rows, cols = len(grid), len(grid[0])

        # Initialize a queue for BFS and a counter for fresh oranges.
        queue = deque()
        fresh_count = 0
      
        # Go through each cell in the grid.
        for i in range(rows):
            for j in range(cols):
                # If we find a rotten orange, add its position to the queue.
                if grid[i][j] == 2:
                    queue.append((i, j))
                # If it's a fresh orange, increment the fresh_count.
                elif grid[i][j] == 1:
                    fresh_count += 1
      
        # Track the number of minutes passed.
        minutes_passed = 0
      
        # Perform BFS until the queue is empty or there are no fresh oranges left.
        while queue and fresh_count > 0:
            # Increment minutes each time we start a new round of BFS.
            minutes_passed += 1
          
            # Loop over all the rotten oranges at the current minute.
            for _ in range(len(queue)):
                i, j = queue.popleft()
              
                # Check the adjacent cells in all four directions.
                for delta_row, delta_col in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    x, y = i + delta_row, j + delta_col
                  
                    # If the adjacent cell has a fresh orange, rot it.
                    # NOTE: the difference between my code in this answeer is this, condition
                    
                    if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 1:
                        fresh_count -= 1
                        grid[x][y] = 2
                        queue.append((x, y))
      
        # If there are no fresh oranges left, return the minutes passed.
        # Otherwise, return -1 because some oranges will never rot.
        return minutes_passed if fresh_count == 0 else -1

    """
        # Count the number of fresh orange, count down
        fresh_oranges = 0

        # Initialize the time counter
        time = 0 # every minute that takes place is an iteration

        # Initialize a queue with the starting rotten orange(s)
        queue = deque()

        # get the dimensions of the grid
        ROWS, COLS = len(grid), len(grid[0])

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append([i, j])
                if grid[i][j] == 1:
                    fresh_oranges += 1

        # Directions in which we can move (Up, down, left, right)
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        # Breadth-first search
        while queue and fresh_oranges > 0:
            # Go through each position at the current level
            for _ in range(len(queue)):
                # Get the positions from the queue
                curr_row, curr_col = queue.popleft()
                # Check all four directions
                for direction_row, direction_col in directions:
                    # Calculate the new position
                    new_row, new_col = curr_row + direction_row, curr_col + direction_col
                    # Check if we are in the grid boundaries and seeing a fresh orange
                    # actually this is the converse situation
                    if (new_row < 0 or new_row == ROWS or new_col < 0 or new_col == COLS or grid[new_row][new_col] != 1):
                        continue
                       
                    grid[new_row][new_col] == 2
                    fresh_oranges -= 1
                    queue.append([new_row, new_col])

            # Increment the time has taken
            time += 1

        # If there is no new path and the number of fresh oranges is still > 0
        return time if fresh_oranges == 0 else -1
        """