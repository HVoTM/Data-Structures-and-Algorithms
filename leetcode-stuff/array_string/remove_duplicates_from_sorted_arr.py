# LEETCODE 26. Remove Duplicates from Sorted Array

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # keeping count of the unique elements, as well as used for index indication 
        k = 0

        # Initialize a dictionary to keep count of the unique occurence
        count = dict()

        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 1
                nums[k] = nums[i]
                k += 1

        return k
    

    def NeetCodeSol(self, nums: List[int]) -> int:
        # starting the left with 1, since there should be an element to be existent 
        l = 1

        for r in range(1, len(nums)):
            # Since the array is arranged in a non-descending order
            # we can just compare with adjacent pairs of elements
            # if the right element is not a duplicate
            # we are sure to have a unique occurence and move the left pointer to the right element and traverse so until the end of array
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return l