
from typing import List
import heapq

class Solution:
    def failedAttempt(self, costs: List[int], k: int, candidates: int) -> int:
 
        left_heap, right_heap = [], []

        for i in range(candidates):
            left_heap.append((costs[i], i))
            right_heap.append((costs[len(costs)-candidates], len(costs)- candidates))

        # Initialize the heaps with *candidates* number of workers for each heap before the first iteration
        heapq.heapify(left_heap)
        heapq.heapify(right_heap)

        total_cost = 0

        # initialize the pointers to shift to the next element
        left, right = candidates-1, len(costs) - candidates
        popped = []
        for i in range(k):
            print("Current iteration:", i, "\n--")

            # Retrieving the smallest element for both
            left_min = left_heap[0]
            right_min = right_heap[0]

            if left_min > right_min:
                left_min, left_min_index = heapq.heappop(right_heap)
                total_cost += left_min
                popped.append(left_min_index)
                # Since we have popped a value from the left heap, we need to retain
                # the values of 
                if right > 0:
                    # Reinserting the values of workers with greater cost
                    while right in popped:
                        right -= 1
                    heapq.heappush(right_heap, costs[right])
            else:
                right_min, right_min_index = heapq.heappop(left_heap)
                total_cost += right_min
                popped.append(right_min_index)
                
                if left < len(costs)-1:
                    left += 1
                    while left in popped:
                        left += 1
                    heapq.heappush(left_heap, costs[left])
            # DEBUG CODE
            print("current right pointer: ", right)
            print("current left pointer: ", left)
            print("Current total cost: ", total_cost)
            print("---------------------------")
        
        return total_cost

costs=[1,2,4,1]
k = 3
candidates=3
solution = Solution()
print('TotalCost: ', solution.totalCost(costs=costs, k=k, candidates=candidates))