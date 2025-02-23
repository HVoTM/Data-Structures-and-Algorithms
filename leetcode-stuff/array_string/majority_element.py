# LEETCODE 169. Majority Elements
# List/arrays

from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # using collections.Counter to make a frequency dictionary for each element in this array
        frequency = Counter(nums)

        # initialzie the threshold to consider an element as the majority element
        threshold = len(nums) // 2

        # check every pairs of key, values with Python dictionary's items() method
        for key, value in frequency.items():
            if value > threshold:
                return key
    
    def followUpSolution(self, nums: List[int]) -> int:
        "Efficient follow-up solution"

        # Adding 3 extra O(1) variables
        threshold = len(nums) // 2
        count = 0
        current_element = nums[0]

        # Sorting takes O(logN)
        nums.sort() # put the array in a non-descending order, this way we can
        # keep count of the number of repeating elements to check
        
        # Iterating over the passed array takes O(N)
        # In short, still takes O(logN + N) -> O(N)
        for num in nums:
            if num == current_element:
                count += 1
                
                # Condition check to make sure the element passes the threshold, given that 
                # its count up to this iteration
                if count > threshold:
                    return num
            
            else:
                current_element = num
                count = 1
    
    # https://www.youtube.com/watch?v=7pnhv842keE&ab_channel=NeetCode
    def NeetCodeSimple(self, nums: List[int]) -> int:
        # create a hashmap (python's dictionary)
        count = {}

        # init the return value, and the maxCount of a certain value as we pass the array in
        res, maxCount = 0, 0

        for n in nums:
            # get(): get the value of n in the array, if there is no n, return 0
            count[n] = 1 + count.get(n, 0)
            res = n if count[n] > maxCount else res
            # continuously update the maxCount with this element's count
            maxCount = max(count[n], maxCount)

        return res
    
    def NeetCodeFollowUp(self, nums: List[int]) -> int:
        """Boyer-Moore algorithm"""
        # IF YOU HAVE SOME DOUBT in the algorithm
        # know that this algorithm depends on the property that the array has a majority element
        
        res, count = 0, 0

        for n in nums:
            # if there is an equal number of count on this element compared to the 
            # res, meaning the res element may not be the majority element
            if count == 0:
                res = n
            
            # keeping count 
            count += (1 if n == res else - 1)
        return res
