# LEETCODE 2542. Maximum SUbsequence Score
# Topics: Greedy, Sorting, Heap(Priority Queue, Array
from typing import List
import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        # Pairing each the elements of nums 1 with its corresponding nums2 value
        # Sort based on nums2 values in a descending order
        pairs = [(n1, n2) for n1, n2 in zip(nums1, nums2)]
        pairs = sorted(pairs, key=lambda p: p[1], reverse=True)

        # Initialize a minHeap to keep track and pop off the smallest value encountered for nums1
        minHeap = []
        n1Sum = 0
        res = 0 

        # Iterating over pairs
        for n1, n2 in pairs:
            # Gradually adding up to the k-subsequence of indices 
            n1Sum += n1
            # We add the iterated value of nums1 to the heap
            heapq.heappush(minHeap, n1)

            # As we pass the threshold of k values needed for the subsequence
            # Pop off the smallest value by using minHeap to identify the values
            if len(minHeap) > k: 
                n1pop = heapq.heappop(minHeap)
                # remove that n1 from the resulting sum
                n1Sum -= n1pop

            # Continuously udpate the next n1sum and check for the maximum score
            # by multiplying with the current n2 (value from nums2)
            if len(minHeap) == k:
                res = max(n1Sum * n2, res)
        return res