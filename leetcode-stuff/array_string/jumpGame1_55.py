# LeetCode 55. Jump Game I
# Topics: Dynamic Programming, Array, Greedy
# https://portal.scitech.au.edu/thitipong/wp-content/uploads/2022/01/Tana_Thanchanok_Jump-Game.pdf

from typing import List

class Solution:
    def __init__(self):
        self.dp = []

    def brute_force(self, nums: List[int]) -> bool:
        """Bruteforce method - O(N^N) time complexity"""
        if (len(nums)) == 0:
            return True
        jumpable = [False] * len(nums)
        jumpable[0] = True
        # Iterate through all the number array
        for i in range(len(nums)):
            # Checking if our current index is reachable given previous iterations
            # we initialize the first index as True for starting
            if (jumpable[i] == False):
                return False
            # For the given max jump steps, we mark the subsequent reachable indices as True for jumpable
            reachable = min(len(nums), i + nums[i] + 1) # this is to check if it is out of the array scope
            for j in range(i+1, reachable):
                jumpable[j] = True
        
        return True
    
    def memoization(self, nums: List[int]) -> bool:
        """
        Top-down approach
        Limitation: recursion depth limit
        """
        # Create an array to collect the result that is already calculated
        memo = [None] * len(nums)
        return self.memoization_util(0, nums, memo)
        
    def memoization_util(self, i: int, nums: List[int], memo):
        # Check base case if reach the end post
        if i >= len(nums)-1:
            return True
        # if the current step is not registered
        elif memo[i] != None:
            return memo[i]
        else:
            # Store the current index False
            memo[i] = False
            for j in range(1, nums[i] + 1):
                if self.memoization_util(j+i, nums, memo):
                    memo[i] = True
                    return True
            return memo[i]
            
    def tabulation(self, nums: List[int]) -> bool:
        self.dp = [False] * len(nums)
        self.dp[0] = True
        for i in range(len(nums)):
            # checking from the furthest jump taken
            for j in range(i-1, -1, -1):
                if (nums[j] + j >= i and self.dp[j] == True): # Check reachable
                    self.dp[i] = True
                    break
        return self.dp[-1]


    def greedy(self, nums: List[int]) -> bool:
        """Greedy solution - O(N) time complexity"""
        # setting the goal post at the end
        goal = len(nums) - 1
        # pass through the array in a reverse order from right to left
        for i in range(len(nums) - 1, -1, -1):
            # Checking if the furthest index (by taking current index i + nums[i], the max number of jumps)
            # reach the current goal
            if (i + nums[i]) >= goal:
                # Shift the goal to the current index
                goal = i
        
        return True if goal == 0 else False