# LEETCODE 1732. Find the Highest Altitude
# TOpic: Array, Prefix Sum
from typing import List
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxAlt = 0
        # The biker starting his trip on point 0, so we start with that
        curr_alt = 0
        for i in range(len(gain)):
            curr_alt += gain[i]
            maxAlt = max(curr_alt, maxAlt)
        return maxAlt