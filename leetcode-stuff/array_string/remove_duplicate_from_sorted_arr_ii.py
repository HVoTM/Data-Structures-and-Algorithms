# LEETCODE 80. Remove Duplicates from Sorted Array II
# pointer

from typing import List

class Solution:
    def AlgoMonsterSolution(self, nums: List[int]) -> int:
        """
        The problem is similar to it precedent problem, but now we allow for the number of elements to occur twice
        """

        # For this problem, we add an additional dictionary to keep count of the number of occurences of a number in the list
        # Extra O(N) memory
        count, k = dict(), 0
        
        # Iterate over the passed array like previously
        for i in range(len(nums)):
            # Check if the element is in the dictionary
            # increment by 1
            if nums[i] in count:
                count[nums[i]] += 1

                # Condition check if this number has occured more than twice (which means there has been 2 duplicates before)
                # we skip to the next iteration
                if count[nums[i]] > 2:
                    continue

            # Update otherwise if not yet encountered
            else:
                count[nums[i]] = 1

            # If the the number has yet to occur more than twice, we add that number to the index of the pointer we are passing into array
            # then shift that pointer to the right by 1, keeping count of the valid subarray simultaneously
            nums[k] = nums[i]
            k += 1

        return k   
    
    # https://algo.monster/liteproblems/80
    def AlgoMonsterSolution(self, nums: List[int]) -> int:
        "which does not add extra memory of a dictionary, which is cool and noteworthy"
        # Initialize the count of unique elements
        unique_count = 0
      
        # Iterate over each number in the input list
        for num in nums:
            # Check if the current number is different from the number
            # at position unique_count - 2. (We are taking advantage of the "non-decreasing" property, so we are ensure that the duplicates are adjacent at most)
            # This is to allow a maximum of two duplicates.
            if unique_count < 2 or num != nums[unique_count - 2]:
                # If condition met, copy the current number to the next position in the array.
                nums[unique_count] = num
                # Increment the count of unique elements.
                unique_count += 1
              
        # Return the length of the array containing no more than two duplicates of each element.
        return unique_count