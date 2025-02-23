# LEETCODE 88. MERGE SORTED ARRAY

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = 0

        for i in range(len(nums1)):
            # detect when the index reaches the empty subarray, that's where we fit the nums2 elements in
            if i >= m:
                nums1[i] = nums2[j]
                j += 1
        nums1.sort()