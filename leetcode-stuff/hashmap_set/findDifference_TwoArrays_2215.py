# LEETCODE 2215. Find the Difference of Two Arrays
# Topics: Hash Table, Array

from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans = []
        
        numlist =[]
        for num in nums1:
            if num not in nums2 and num not in numlist:
                numlist.append(num)
        ans.append(numlist)
        numlist = []
        for num in nums2:
            if num not in nums1 and num not in numlist:
                numlist.append(num)
        ans.append(numlist)
        "Space: O(N), Time: O(N)"
        return ans

    def NeetCode_solution(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # Turning the arrays into sets so they will only contain unique elements (remove duplicates)
        # That is the property of a set
        nums1Set, nums2Set = set(nums1), set(nums2)
        # Initialize two empty (hash) sets for each set
        res1, res2 = set(), set()

        for n in nums1:
            # Add the set so they do not contain duplicates even if you add it multiple time
            if n not in nums2Set:
                res1.add(n)
        for n in nums2:
            if n not in nums1Set:
                res2.add(n)
        # Typecasting the set back into list
        return [list(res1), list(res2)]