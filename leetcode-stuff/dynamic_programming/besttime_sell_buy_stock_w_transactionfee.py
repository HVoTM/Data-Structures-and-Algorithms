# LEETCODE 714. Best Time to Buy and Sell Stock with Transaction Fee
# TOPic: Dynamic Programming, Array, Greedy

from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # https://algo.monster/liteproblems/714
        # Initialize cash and hold variables:
        # cash represents the max profit achievable without holding any stock
        # hold represents the max profit achievable while holding a stock
        cash, hold = 0, -prices[0]
      
        # Iterate through the list of prices, starting from the second price
        for price in prices[1:]:
            # Update cash to the max of itself or the profit from selling a stock at the current price minus the fee
            # Update hold to the max of itself or the value of the cash after buying a stock at the current price
            cash, hold = max(cash, hold + price - fee), max(hold, cash - price)
      
        # The value of cash at the end of iteration will represent the maximum profit achievable
        return cash

    def memoizationApproach(self, prices: List[int], fee: int) -> int:
        # Initialize a memoization array to stor the results of dfs(i, j)
        memo = {}

        # Defining the utility function of recursion to pass the prices[] through
        # and define possible outcomes
        def dfs(i, holding):
            if i >= len(prices):
                return 0 # Base case: no more transactions possible
            
            if (i, holding) in memo:
                return memo[(i, holding)]
            
            # If we are not holding a stock
            if holding == 0:
                # Either skip this day or buy a stock
                memo[(i, holding)] = max(dfs(i+1, 0), -prices[i] + dfs(i+1, 1))

            # If we are holding a stock
            elif holding == 1:
                # Either skip this day or sell the stock
                # we return the maximum profit
                memo[(i, holding)] = max(dfs(i+1, 1), prices[i] + dfs(i+1, 0) - fee)

            return memo[(i, holding)]
        return dfs(0, 0)
