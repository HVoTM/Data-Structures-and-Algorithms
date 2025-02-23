# LEETCODE 162 - Binary Search - Find PEak Element
from typing import List

class Solution:
    # https://www.youtube.com/watch?v=kMzJy9es7Hc&ab_channel=NeetCodeIO
    def findPeakElement(self, nums: List[int]) -> int:
    # Concepts: monotonically increasing/decreasing
        # initialize counters for binary search
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left)//2 # guarantees prevention of overflow, 
            # mostly does not appear in coding interviews but it is good to know
            
            # left neighbor greater
            if mid > 0 and nums[mid] < nums[mid-1]: # check if the middle index is out of bounds
                # update for the pointers to shift to the left side
                right = mid -1
            # right neighbor greater, the other cases
            elif mid < len(nums)-1 and nums[mid] < nums[mid+1]:
                left = mid + 1

            else:
                # in this case, if left equals right
                # the array is "monotonically" balanced, then we can return either index 0 or len(nums) - 1
                return mid