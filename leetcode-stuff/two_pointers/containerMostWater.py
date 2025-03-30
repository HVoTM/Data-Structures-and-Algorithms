from typing import List
# LEETCODE 11. Container With Most Water
# Topic: Two Pointers, Array, Greedy

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Initialize answer to iterate over, the left and right pointers
        res = 0
        l, r = 0, len(height) - 1

        # Loop 
        while l < r:
            # Computing the area of the current l, r pointers: distance between the pointers and the height of the smaller line
            area = (r - l) * min(height[l], height[r])
            # Retain the largest area at the moment
            res = max(res, area)

            # Compare between the two heights of the pointer and shift the index of the shorter end inwards
            # Intuitionwise, keeping the pointer at the taller line stationary and moving the shorter one might lead
            # us to find a taller line and thus a larger area. Simply that bcuz there is no advantage in moving the 
            # taller pointer first
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return res