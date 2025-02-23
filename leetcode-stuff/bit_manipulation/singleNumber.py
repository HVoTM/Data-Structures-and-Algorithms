# LEETCODE 136. SIngle Number
# Topic: Bit Manipulation

from typing import List
from functools import reduce  # Import reduce from functools module
from operator import xor  # Import bitwise xor operator

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        "https://www.youtube.com/watch?v=qMPX1AOa83k&ab_channel=NeetCode"
        # Initialize 0 as a check value, since this is a non-empty array, we can make sure that
        # there should be a valid element 
        res = 0
        for n in nums:
            # perform bitwise XOR with the current res with the passed value
            # the idea is to use bitwise XOR (^) to eliminate all doubly occuring elements
            # by nullifying the bits (in the corresponding significant order) to 0
            # leaving behind when we compare with the single element to be compare
            # it will return correspondingly
            # ORder does not matter in this case
            # I know, I am not wholly satisfied with the explanation as well
            # Will go back if needed further inspection or deem it as highly important in my studying
            res = n ^ res
        return res
    
    def AlgoMonster(self, nums: List[int]) -> int:
        "https://algo.monster/liteproblems/136"
        # This method finds the element that appears only once in an array
        # where every other element appears exactly twice.
      
        # It applies the reduce function to perform a cumulative xor operation 
        # over all the numbers in the list. The xor of a number with itself is 0,
        # and the xor of a number with 0 is the number itself. Thus, only the 
        # element that appears once will remain after the reduction.
      
        return reduce(xor, nums)