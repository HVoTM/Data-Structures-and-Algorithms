# LEETCODE 1679. Maximum pnumber of K-Sum pairs
# Helped by https://algo.monster/liteproblems/1679

from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        "Concepts: sorted list, two pointers"
        # Sort the array first to apply the two pointer technique
        nums.sort()
        # max operations to be executable on this array for k
        ans = 0
        
        # initialize the two pointers
        left, right = 0, len(nums) - 1

        while left < right:
            curr_sum = nums[left] + nums[right]
            if curr_sum == k:
                ans += 1
                right -= 1
                left += 1
            # sorting the list conveniently let us pass to the adjacent value knowing that the sum is
            # insufficient or overreaching for the known k
            # so we can pass to the next value
            elif curr_sum > k:
                right -= 1
            elif curr_sum < k:
                left += 1
        return ans

        "space: O(logN) due to sorting, time: O(nlogn) becasue of the sorting step (scanning step is O(n))"


