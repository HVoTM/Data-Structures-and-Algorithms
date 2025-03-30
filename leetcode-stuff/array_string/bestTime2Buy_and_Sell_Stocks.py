# LEETCODE 121: Best Time to Buy and Sell Stock
# TOpics: Array, Dynamic Programming

from typing import List

# Here we will be using the two-pointer approach

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        "BUY LOW, SELL HIGH"
        l, r = 0, 1
        ans = 0
        while r < len(prices):
            # Profitable? 
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                # Assign the result with the maximum profit
                ans = max(profit, ans)
            else:
                # we want to shift it all the way to the right
                # This condition is guaranteed because for the other case, we will just keep finding pointers
                # that have prices that are larger than the current left's price
                # so if we were to encounter one smaller, we can do a greedy asignment on that current right pointer's index
                l = r
            
            r += 1
        
        return ans
