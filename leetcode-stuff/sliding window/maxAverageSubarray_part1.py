# LEETCODE 643. Maximum Average Subarray I
# https://leetcode.com/problems/maximum-average-subarray-i/
# TOpics: Array, Sliding Window

from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSum = 0
        # edge case
        if len(nums) <= k:
            return sum(nums)/float(len(nums))
        
        # Compute the first window of size k, for python list[i:k] will retrieve index ith to index (k-1)th
        currentWindowSum = sum(nums[:k])
        # Compute the sums of remaining windows by removing first element of previous
        # window and adding last element of the current window.
        maxSum = currentWindowSum

        # Using the sliding window method, we will just keep popping the leftmost element and insert the rightmost element
        for i in range(len(nums)-k):
            currentWindowSum = currentWindowSum - nums[i] + nums[i+k]
            maxSum = max(maxSum, currentWindowSum)
        
        return maxSum/float(k)
        
        "Runtime: O(N), Space: O(1)"
        
        
        