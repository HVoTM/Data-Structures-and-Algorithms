# LEETCODE 724. Find Pivot Index
# Topics: Array, Prefix Sum
from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Initial left sum
        leftSum = 0
        # Get the total sum of this array
        totalSum = sum(nums)

        # Iterate and pass through the array
        for i in range(len(nums)):
            # We concurrently calculate the rightsum by deducting the leftsum and current index 
            rightSum = totalSum - nums[i] - leftSum
            # Pivot index found?
            if rightSum == leftSum:
                return i
            # leftsum is initialized 0 (as the left edge) for the first iteration, so now we continuously
            # add the current index's value for the next turn  
            leftSum += nums[i]
        return -1