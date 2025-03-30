# LEETCODE 122. Best time to Buy and Sell Stocks II
# Topic: array, dynamic programming, greedy

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        # Feels very tricky at first, but it is just buying and selling at the day that has a higher price
        for i in range(1, len(prices)):
            # Just mean you buy and sell at the soonest higher selling prices as many time as possible
            # Do not wait for the highest price, that's it
            if prices[i] > prices[i-1]:
                ans += prices[i] - prices[i-1]
        return ans
