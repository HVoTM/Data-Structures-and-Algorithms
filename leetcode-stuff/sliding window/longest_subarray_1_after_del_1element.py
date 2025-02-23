# LEETCODE 1493. Longest Subarray of 1's After Deleting 1 Element
# Sliding Window, Dynamic PRogramming

from typing import List


class Solution:
    
    def LeetCode(self, nums: List[int]) -> int:
        "This LeetCode solution (i think i got a free solution access for this one) applies the usual sliding window approach"
        # the number of zero's in the window
        zeroCount = 0
        longestWindow = 0

        # left pointer
        start = 0

        # i here can be seen as a right pointer (drop-dead just name it r or something)
        for i in range(len(nums)):
            zeroCount += (nums[i] == 0)

            # Shrink the window until the count of zero's is less than
            # or equal to 1, since the problem allows an extra 0 to be dropped
            while (zeroCount > 1):
                # this is to check if the element at that left pointer is still 0
                zeroCount -= (nums[start]==0)
                start += 1
            
            # for every iteration compare the size of the current longest window with the longest subarray 
            # we have so far as the subtraction of right to left pointer
            longestWindow = max(longestWindow, i - start)

        return longestWindow
    
    def AlgoMonster(self, nums: List[int]) -> int:
        # https://algo.monster/liteproblems/1493
        "This problem uses an approach relating dynamic programming"
        # Determine the length of the nums list
        n = len(nums)

        # Initialize two lists to keep track of consecutive ones to the left and right of each index
        left_ones_count = [0] * n
        right_ones_count = [0] * n

        # Calculate the consecutive ones to the left of each index
        for i in range(1, n):
            if nums[i - 1] == 1:
                left_ones_count[i] = left_ones_count[i - 1] + 1

        # Calculate the consecutive ones to the right of each index
        for i in range(n - 2, -1, -1):
            if nums[i + 1] == 1:
                right_ones_count[i] = right_ones_count[i + 1] + 1

        # Find the maximum length subarray formed by summing up counts of left and right ones.
        # Note that the question assumes we can remove one zero to maximize the length.
        # So, connecting two streaks of ones effectively means removing one zero between them.
        max_length = max(a + b for a, b in zip(left_ones_count, right_ones_count))


        return max_length
    
    def mySolution(self, nums: List[int]) -> int:

        """
        Technically, this solution works, but I think there is a caveat or a discrepancy in the logic
        , or I am just not getting it. (FYI, the solution here is just the variant of the solution 
        for problem 1004 but with k = 1)

        some questions I am still pondering:
        - what if there is a subarray with the longest consecutive 1's that can be made without the need of dropping a 0
        - an array full of 1's, so no need to drop
        """
        # Initialize the left, right pointer at the end of the array
        left = right = -1
        k = 1
        while right < len(nums) - 1:
            right += 1

            if nums[right] == 0:
                k -= 1

            if k < 0:
                left += 1

                if nums[left] == 0:
                    k += 1

        return right - left -1
    