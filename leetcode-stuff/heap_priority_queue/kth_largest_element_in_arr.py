# LEETCODE 215. k-th Largest Element in the Array
# TOpic: Array, Divide and Conquer, Sorting, Heap (priority queue), Quickselect

from typing import List
import heapq

class findthKthLargest:
    def naive(self, nums: List[int], k: int) -> int:
        """The naive approach is to sort the list and index the required element"""
        nums.sort(reverse = True)

        return nums[k - 1]
    """
        nums.sort()
        return nums[len(nums) - k]
    """
    
    def minHeap(self, nums: List[int], k: int) -> int:
        """Using Min-heap and priority queue to pass the array in O(N) time"""
        # Min heap to store the K largest element
        pq = []

         # Iterate through the array elements
        for val in nums:
        
            # Add current element to the min heap
            heapq.heappush(pq, val)
            
            # If heap exceeds size K, remove smallest element
            if len(pq) > k:
                heapq.heappop(pq)

        # Top of the heap is the K'th largest element
        return pq[0]
    

    def quickSelect(self, nums: List[int], k: int) -> int:
        """Another approach using the quickselect approach, which is similar to 
        partitioning part in the quicksort algorithm
        """
        # Quickselect: average case - O(N) - is faster than the sorting solution - O(NlogN)
        # https://www.youtube.com/watch?v=XEmy13g1Qxc&ab_channel=NeetCode
        
        # We want to put the values in ascending order (left to right)
        # so we complement by getting the subtraction of this array's length by k 
        k = len(nums) - k

        # quickSelect function with inputs of left and right pointers
        def quickSelect(l ,r):
            # defining the pivot value with the pivot pointer as the left pointer
            pivot, p = nums[r], l
            
            # checking for the elements in the passed array with index from left to right pointer
            # as the partition part to be compared
            for i in range(l, r):
                # Checking if the passed value is smaller than the pivot value
                # we perform a swap to the current i-th pointer in that array
                # values that are larger than the pivot value will remained unchanged
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    # increment the next element to be swapped
                    p += 1
            
            # Swap the pivot value with the p-indexed value
            nums[p], nums[r] = nums[r], nums[p]

            # if have yet to find the kth largest element:
            # find the left side as pivot is still larger than the required k
            # recursively call the function again
            if p > k:
                return quickSelect(l, p - 1)

            # the other case
            elif p < k: 
                return quickSelect(p + 1, r)
            
            # if found p==k, return the result
            else: return nums[p]

        return quickSelect(0, len(nums) - 1)