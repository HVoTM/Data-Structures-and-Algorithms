# LEETCODE 452. Minimum Number of Arrows to Burst Balloons
# Topics: Array, Greedy, Sorting

from typing import List
"NOTE: this problem is the same as non-overlapping intervals, just phrased differently with a different request"
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Sort the balloons x-interval points by ascending order 
        points.sort()
        # Initialize the answer to return, since we will be including the first balloon in
        # so the initial count would be 1 since there is already a balloon to burst
        ans: int = 1
        # Retrieve the starting and ending x-coordinate of the first arranged balloon
        prevEnd = points[0][1]
        # Check with the sequential balloons in the point
        for start, end in points[1:]:
            # If the next balloon has a starting x-coordinate greater than the current prevEnd
            if start > prevEnd:
                # Increment count for the additional arrow usage
                ans += 1
                # Mark the end point of this current balloon to be the new prevEnd
                prevEnd = end
            else:
                # If the current balloon is still in the interval range of the current arrow
                # we take the smaller out of the compared end point to ensure that 
                # the new balloon is still in the range of bursting
                prevEnd = min(prevEnd, end)

        return ans