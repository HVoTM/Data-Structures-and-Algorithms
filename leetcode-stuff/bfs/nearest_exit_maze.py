# LEETCODE 1926. Nearest Exit from Entrance in Maze
# Graph - BFS 

# Used concepts
"""
Queue (deque): A queue is used for the BFS traversal, which follows the First-In-First-Out (FIFO) principle. 
This ensures that cells are explored in the order they are reached.

Visited Marking: When a cell is visited, it is marked by changing its value to '+'. 
This prevents the algorithm from re-visiting the same cell, which would otherwise lead to infinite loops and incorrect step count.

Direction Array: A simple 2D array [[0, -1], [0, 1], [-1, 0], [1, 0]] is used to 
represent the four possible moves from any cell (left, right, up, down).

Checking Exit Condition: An exit is an empty cell ('.') at the border of the maze. Whenever moving to a new cell,
the algorithm checks if it is an exit by comparing its coordinates with the boundary of the maze.

Steps Counter: The variable ans is used to count the number of steps taken to reach an exit. 
It gets incremented at the start of processing each level, ensuring the correct step count when an exit is found.
"""

from typing import List
from collections import deque
# help: https://algo.monster/liteproblems/1926
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # exit means that there is a boundary cell that has "."
        # boundary cells are:
        # maze[0][i]/ maze[i][0] / maze[m-1][i] / maze[i][n-1]
        # m, n: the shape of the maze, largest column/row index
        # i: any of the cell that is in range of the maze

        # trace back from the exit to the current entrance
        # movement: row/col +/- i (up/down/left/right)

        # Step 1: create a graph to connect the accessible pathway in the tree
        # Step 2: use bfs to count the number of shortest possible exit

        # Get the dimensions of the maze
        rows, cols = len(maze), len(maze[0]) 
        
        # Get the entrance coordinates
        row_entrance, col_entrance = entrance 
        # row_entrance, col_entrance = entrance[0], entrance[1]

        # Initialize a queu with the starting position (entrance)
        queue = deque([(row_entrance, col_entrance)])

        # Mark the starting position as visited by changing its value to '+'
        maze[row_entrance][col_entrance] = '+'

        # Initialize the number of steps taken to exit
        steps = 0

        # BFS loop
        while queue:
            # Increment the steps at the start of the current level
            steps += 1

            # Go through each position at the current level
            for _ in range(len(queue)):
                # Get positions from queue
                curr_row, curr_col = queue.popleft()

                # Directions in which we can move: left, right, up, down
                directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]

                # Check all four directions
                # NOTE: as we pass for each element in the array, we can unpack like this
                for direction_row, direction_col in directions:
                    # Calculate new positoin
                    new_row, new_col = curr_row + direction_row, curr_col + direction_col

                    # Check if the new position is within the maze boundaries
                    # and if it has not been visited (maze cell is '.')
                    if 0 <= new_row < rows and 0 <= new_col < cols and maze[new_row][new_col] == '.':
                        # Check if the new position is on the edge of the maze,
                        # which means an exit is found
                        if new_row == 0 or new_row == rows - 1 or new_col == 0 or new_col == cols - 1:
                            return steps
                      
                        # Otherwise, add the position to the queue and mark as visited
                        queue.append((new_row, new_col))
                        maze[new_row][new_col] = '+'
      
        # If we have not found an exit, return -1 indicating failure to find an exit
        return -1