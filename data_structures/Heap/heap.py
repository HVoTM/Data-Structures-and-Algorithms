from heapq import heapify, heappop, heappush
from typing import Optional, Tuple
"""
Heap is a complete binary tree that can be represented as an array
- MinHeap: root must be the smallest among all nodes in the array, every children nodes are greater 
than their parent nodes
- MaxHeap: the opposite of min-heap, the largest being the root, all children nodes are 
smaller than the parents
- root element will be at the 0th index of the array
- 

# Time complexity analysis
- getMin(): O(1)
- extractMin(): O(logN) as the operation needs to maintain the heap property
by calling the `heapq.heapify()`
- decreaseKey(): O(logN), traverse up the heap to maintain heap property
- insert(): O(logN), add then heapify
- delete(): O(logN), same as extractMin except that we are deleting inside the tree structure

"""
class MinHeap:

    def __init__(self):
        # initialize the priority queue variable
        self.heap = []
    
    def getParent(self, index) -> int:
        return (index - 1) / 2
    
    def getLeftChild(self, index) -> int:
        return (2*index) + 1
    
    def getRightChild(self, index) -> int:
        return (2*index) + 2
    
    def getChildren(self, index) -> Tuple[int]:
        return 2*index+1, 2*index+2
    
    def hasParent(self, index):
        # getting the parent node will return a smaller index than the current index
        return self.getParent(index) >= 0

    def hasLeftChild(self, index) -> bool:
        # checking the child node as it has a larger index value 
        return self.getLeftChild(index) < len(self.heap)
    
    def hasRightChild(self ,index) -> bool:
        return self.getRightChild(index) < len(self.heap)
    
    # Operations to work around the binary tree
    def getMin(self):
        """Operation to retrieve the value but not taking it out of the tree"""
        return self.heap[0]

    def extractMin(self):
        """Retrieve the root and pop the node from the tree"""
        return heappop(self.heap)

    def insertKey(self, k):
        heappush(self.heap, k)

    def decreaseKey(self, i, new_val):
        self.heap[i]  = new_val 
        while(i != 0 and self.heap[self.parent(i)] > self.heap[i]):
            # Swap heap[i] with heap[parent(i)]
            self.heap[i] , self.heap[self.getParent(i)] = (
            self.heap[self.getParent(i)], self.heap[i])
    

