# Python code implementing max Heap 

class MaxHeap:
    # Declaring all the basic heap properties
    def __init__(self) -> None:
        self.heap = []
    
    # Getting parent index by returning the lower value of index / 2
    # We will shift the index to the left by 1 bit position
    def get_parent_index(self, index) -> int:
        return (index - 1) // 2

    # As the bit shift representation has changed, we will also implement
    # get left and right child the same way, by adding 1 for those two
    def get_left_child_index(self, index) -> int:
        return 2 * index + 1

    def get_right_child_index(self, index) -> int:
        return 2 * index + 2

    # Basic methods to verify the existence of a parent or child of an index
    def has_parent(self, index) -> bool:
        return self.get_parent_index(index) >= 0

    def has_left_child(self, index) -> bool:
        return self.get_left_child_index(index) < len(self.heap)

    def has_right_child(self, index) -> bool:
        return self.get_right_child_index(index) < len(self.heap)
    
    def swap(self, index1, index2) -> None:
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
    
    # heapify_up: This method ensures that the heap property 
    # is maintained by moving an element up the heap to its correct position 
    # if it violates the max-heap property.

    def heapify_up(self, index):
        while self.has_parent(index) and self.heap[index] > self.heap[self.get_parent_index(index)]:
            self.swap(index, self.get_parent_index(index))
            index = self.get_parent_index(index)

    # heapify_down: This method ensures that the heap property 
    # is maintained by moving an element down the heap to its correct position 
    # if it violates the max-heap property.

    def heapify_down(self, index):
        while self.has_left_child(index):
            max_child_index = self.get_left_child_index(index)
            if (self.has_right_child(index) and 
                self.heap[self.get_right_child_index(index)] > self.heap[max_child_index]):
                max_child_index = self.get_right_child_index(index)

            if self.heap[index] < self.heap[max_child_index]:
                self.swap(index, max_child_index)
                index = max_child_index
            else:
                break
    
    # Add a new element to the heap
    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    # extract_max: This method removes and 
    # returns the maximum element from the heap.
    def extract_max(self):
        if len(self.heap) == 0:
            return None

        max_value = self.heap[0]
        last_index = len(self.heap) - 1
        self.swap(0, last_index)
        del self.heap[last_index]

        self.heapify_down(0)

        return max_value

    # Method to return the max value without removing the element
    def peek(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]