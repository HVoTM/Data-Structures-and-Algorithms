# The common method in implementing Priority Queue in Python
"""
Here the Priority Queue is the common type of Priority Queue we are using, which will be implementing min-heap
the smaller the priority we take.

Reference from document:a

When using heapq with a tuple, the comparison is done lexicographically. This means that 
the first element of the tuple is used as the primary key for comparison. 
If there is a tie, the second element is considered, and so on.

So for A = node(1, 'Task 4') and B = node(3, 'Task 6') -> heapq will consider A before B
to maintain heap invariant

To implement Max Priority Queue:
Which will be not of much usage in practice, just consider priority 
as (-1) * priority when inserting into heap.
"""
import heapq 
# heapq module which provides heap queue algorithm, for more information on 
# related methods: type: python >> import heapq; help(heapq)
# or:  https://docs.python.org/3.11/library/heapq.html

class MaxPriorityQueue:
    # Initializing the heap
    def __init__(self) -> None:
        self.heap = []
    
    # heapify: function to initialize a heap using a provided list
    def heapify(self, newlist):
        self.heap = [(priority, item) for priority, item in newlist]
        heapq.heapify(self.heap) # transform it into a heap, maintaining the heap invariant
    
    def insert(self, priority, item):
        heapq.heappush(self.heap, (priority, item)) # taking in a tuple containing priority and item
        # heappush will consider priority then item if first comparison, the priorities, is equalled
        # also maintaining the heap invariant
    
    # Here the pop function will be implemented to pop the top value
    # Notice: heapq.heappop will extract the smallest item from the heap.
    def extract(self):
        if not self.is_empty():
            priority, item = heapq.heappop(self.heap)
            # Similarly, heappop will remove and return the smallest element
            # considering the first element as priority then item next.
            return item
        else:
            raise IndexError('empty priority queue!!!') # or return None should suffice
            
    def peek(self):
        if not self.is_empty():
            priority, item = self.heap[0]
            return item
        else:
            return None
  
    def changePriority(self, item_to_change, newpriority):
        # Create a temporary heap with list comprehension
        # For more info on list comprehension: 5.1.3 here https://docs.python.org/3/tutorial/datastructures.html
        temp_heap = [(priority, item) for priority, item in self.heap if item != item_to_change]
        heapq.heappush(temp_heap, (newpriority, item_to_change))
        self.heap = temp_heap

    def is_empty(self) -> bool:
        return len(self.heap) == 0
    
# Example usage:
initial_list = [(10, "Task 1"), (5, "Task 2"), (8, "Task 3")]

pq = MaxPriorityQueue()
pq.heapify(initial_list)

print(pq.peek())  # Output: Task 2
print(pq.extract())   # Output: Task 2

pq.insert(7, "Task 4")
pq.insert(12, "Task 5")
pq.insert(4, "Task 6")

print(pq.peek())  
print(pq.extract())  # Output: task 6

print(pq.peek()) 
print(pq.extract()) # Output: task 4

# Testing the ChangePriority function

# Inserting the old items
pq.insert(7, "Task 4")
pq.insert(12, "Task 5")
pq.insert(4, "Task 6")

print("Original priority queue:")
for priority, item in pq.heap:
    print(item)

# Change the priority of 'Task 1' to 0, put it at the top
pq.changePriority('Task 1', 0)

print("\nPriority queue after changing priority:")
while not pq.is_empty():
    print(pq.extract())
