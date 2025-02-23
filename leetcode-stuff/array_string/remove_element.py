# LEETCODE 27. Remove Elements

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        right = len(nums) - 1
        for i in range(len(nums)):
            if nums[i] != val:
                k += 1
            else:
                nums[i] = float(inf)
        nums.sort()
        return k
    
    def NeetCodeSolution(self, nums: List[int], val: int) -> int:
        "https://www.youtube.com/watch?v=Pcd1ii9P9ZI&ab_channel=NeetCode"

        # initialize the return answer
        k = 0

        right = len(nums) - 1
        for i in range(len(nums)):
            if nums[i] != val:
                # somuch easier, we just put the proper element that suits the condition into the the incrementing
                # first k values that are not equal to val
                nums[k] = nums[i]
                k += 1
        return k