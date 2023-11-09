# HEAPS DATA STRUCTURES

# Class to Implement Heaps
    # Reminder:  This method signature explicitly provides a type hint that __init__ returns None
    # Basically, it's good practice in Python to code more self-documenting and
    # helps code analysis tools and developers understand the expected behavior of the method.

class MinHeap:
    def __init__(self) -> None:
        self.heap = []

    def get_parent_index(self, index):
        return (index - 1) // 2

    def get_left_child_index(self, index):
        return 2 * index + 1

    def get_right_child_index(self, index):
        return 2 * index + 2

    def has_parent(self, index):
        return self.get_parent_index(index) >= 0

    def has_left_child(self, index):
        return self.get_left_child_index(index) < len(self.heap)

    def has_right_child(self, index):
        return self.get_right_child_index(index) < len(self.heap)

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def heapify_up(self, index):
        while self.has_parent(index) and self.heap[index] < self.heap[self.get_parent_index(index)]:
            parent_index = self.get_parent_index(index)
            self.swap(index, parent_index)
            index = parent_index

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

    def insert(self, item):
        self.heap.append(item)
        self.heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if len(self.heap) == 0:
            return None

        min_element = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self.heapify_down(0)
        return min_element

    def peek(self):
        if self.heap:
            return self.heap[0]
        return None
