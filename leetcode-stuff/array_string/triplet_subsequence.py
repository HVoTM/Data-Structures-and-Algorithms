# LEETCODE 334. Increasing Triplet Subsequence
# for this code, we are using a greedylike method to compare the middle value as we pass along the array from left to right
# initialize the smallest element and middle element to infinity and compare within the trailing array
# if we come across an element that serves with the conditions, assign to it correspondingly
# succcessfully found a triplet if we find an element later in the array that is larger than the current middle value that has been assigned
# an actual value from the element

from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # Initialize two variables with infinity which will
        # represent the smallest and middle numbers of the triplet.
        smallest = float('inf')
        middle = float('inf')

        # Iterate over the list of numbers.
        for num in nums:
            # If current number is greater than the middle number,
            # an increasing triplet exists.
            if num > middle:
                return True
          
            # If current number is less than or equal to the smallest,
            # update the smallest number to be the current number.
            if num <= smallest:
                smallest = num
            # Otherwise, if the current number is between the smallest
            # and the middle, update the middle number.
            else:
                middle = num

        # Return False if no increasing triplet is found.
        return False
