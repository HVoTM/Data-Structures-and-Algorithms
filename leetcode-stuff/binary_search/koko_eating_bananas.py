# LEETCODE 875 - Koko Eating Bananas - Binary search
from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # https://www.youtube.com/watch?v=U2SozAs9RzA&ab_channel=NeetCode
        # Initialize left and right pointers for binary search
        # here we are counting down from the max number of bananas we can eat, which is the max value in the list
        # then check the descending values if eating fewer bananas can still fit in h hours
        l, r = 1, max(piles)

        # temporarily assign the max to result
        res = r

        # Perform binary search method
        while l <= r:
            # middle value
            k = (l + r) // 2
            # Counting the number of hours take if k (number of bananas eaten / hour) 
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k) # NOTE. math.ceil()

            # if the current duration take less time than the proposed h hours
            # we can even go fewer bananas per hour 
            if hours <= h:
                res = min(res, k)
                r = k - 1
            # eating the current k takes more than h hours, go higher number of bananas per hour
            else:
                l = k + 1
            # Continue looping until we find the minimum k that fits in the h hours
        return res
