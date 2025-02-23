# LEETCODE 435. Non-overlapping Intervals
# Topics: Array, Dynamic Programming, Greedy, Sorting

from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        "https://www.youtube.com/watch?v=nONCGxWoUfM&ab_channel=NeetCode"
        "We will be following the greedy method approach"
        # Sort the intervals
        # (Python will automatically sort the elements in a list of lists by comparing the first element of each
        # then move on to the next one if it cannot decide the sequencing order)
        intervals.sort()
        ans = 0
        # Set the initial end point of the smallest ordered interval for comparison
        prevEnd = intervals[0][1]
        # Given the order we have set, we just need to compare the subsequential adjacent intervals from then on
        for start, end in intervals[1: ]:
            # if the current interval has a greater start point than prevEnd
            # set prevEnd to the current end point 
            if start >= prevEnd:
                prevEnd = end
            # Increment the number of minimum step by one
            else:
                ans += 1
                # Greedy method approach: To preserve the minimum number of intervals to be removed 
                # we take the smaller between the compared end points since smaller end points will maintain
                # the number of small intervals to still be included
                # so only the interval with the largest range is to be removed  
                prevEnd = min(prevEnd, end)
        
        return ans
