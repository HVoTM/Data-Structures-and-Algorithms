# HEAPS DATA STRUCTURES

# Class to Implement Heaps
    # Reminder:  This method signature explicitly provides a type hint that __init__ returns None
    # Basically, it's good practice in Python to code more self-documenting and
    # helps code analysis tools and developers understand the expected behavior of the method.

class MinHeap:
    def __init__(self) -> None:
        self.heap = []

    # Basic methods to return the indices of any parent/child
    # already explained as well about the operations for shifting the bit representation by 1 for the index
    # look up in MaxHeap class
    def get_parent_index(self, index):
        return (index - 1) // 2

    def get_left_child_index(self, index):
        return 2 * index + 1

    def get_right_child_index(self, index):
        return 2 * index + 2

    # Basic methods to verify the existence of an index's parent/child
    def has_parent(self, index):
        return self.get_parent_index(index) >= 0

    def has_left_child(self, index):
        return self.get_left_child_index(index) < len(self.heap)

    def has_right_child(self, index):
        return self.get_right_child_index(index) < len(self.heap)
    
    # Fundamental swap functions to use in the heapify function
    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    # heapify_up: This method to ensure the heap property
    # is maintained by moving an element up the correct position
    # if it violates the minheap property
    def heapify_up(self, index):
        while self.has_parent(index) and self.heap[index] < self.heap[self.get_parent_index(index)]:
            parent_index = self.get_parent_index(index)
            self.swap(index, parent_index)
            index = parent_index

    # heapify_down: The method to ensure the heap property is maintained
    # by moving an element down the heap to the correct position 
    # if it violates the minheap property. Here iteratively 
    # go down the heap until we have the correct placement
    def heapify_down(self, index):
        while self.has_left_child(index):
            smaller_child_index = self.get_left_child_index(index)
            if self.has_right_child(index) and self.heap[self.get_right_child_index(index)] < self.heap[smaller_child_index]:
                smaller_child_index = self.get_right_child_index(index)

            if self.heap[index] < self.heap[smaller_child_index]:
                break
            else:
                self.swap(index, smaller_child_index)

            index = smaller_child_index

    # Insert method to add an item to the list representation
    # we heapify up since it's initially placed last until 
    # the it gets the correct position
    def insert(self, item):
        self.heap.append(item)
        self.heapify_up(len(self.heap) - 1)

    # Method to remove and return the minimum element from the heap
    def extract_min(self):
        if len(self.heap) == 0:
            return None

        # Get the minimum value, which is at the top of the heap
        min_element = self.heap[0]

        # Swap the root (maximum element) with the last element in the heap
        last_index = len(self.heap) - 1
        self.swap(0, last_index)

        del self.heap[-1]  # Delete the last element

        # Heapify-down starting from the root to rearrange the heap
        # while maintaining the heap
        self.heapify_down(0)

        return min_element
    
    # peek: method to return the minimum value, without removing the element
    # itself from the heap
    def peek(self):
        if self.heap:
            return self.heap[0]
        return None
