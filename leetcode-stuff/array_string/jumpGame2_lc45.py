# Leetcode 45. Jump Game II
#Topics: Array, Dynamic Programming, Greedy
# NOTE: you can always reach the last index, given the problem statement
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        """Greedy Solution with help from NeetCode - makes the locally optimal choice"""
        ans = 0 
        # Initialize two pointers to represent a window of the array
        l = r = 0
        """Simplifed BFS on a 1D array - time O(N)"""
        while r < (len(nums) -1):
            # For the current l, r indices
            farthest = 0
            for i in range(l, r+1): # make the right value inclusive
                # Check on what is the farthest index we can reach given all the indices in the window
                farthest = max(farthest, i + nums[i])
            # Shift the current window by expanding right to the farthest location we have computed
            # and left as the index after the previous right
            l = r + 1
            r = farthest
            # For every window update, we increment the count
            ans += 1
            # We continue to search for the farthest index we can reach within the new window
            # In a way, we do not need backtracking if the farthest we compute somehow takes more jumps
        return ans
    
    def jump_AlgoMonster(self, nums: List[int]) -> int:
        # https://algo.monster/liteproblems/45
        # Initialize the jump count, the maximum reach, and the edge of the current range to 0.
        jump_count = max_reach = last_reach = 0
      
        # Iterate over the list excluding the last element as it's unnecessary to jump from the last position.
        for index, value in enumerate(nums[:-1]):
            # Update the maximum reach with the furthest position we can get to from the current index.
            max_reach = max(max_reach, index + value)
          
            # If we have reached the furthest point to which we had jumped previously,
            # Increment the jump count and update the last reached position to the current max_reach.
            if last_reach == index:
                jump_count += 1
                last_reach = max_reach
      
        # Return the minimum number of jumps needed to reach the end of the list.
        return jump_count
