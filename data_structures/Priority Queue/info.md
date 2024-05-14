# Definition
A priority queue is a type of queue that arranges elements based on their priority values. Elements with higher priority values are typically retrieved before elements with lower priority values.

In a priority queue, each element has a priority value associated with it. When you add an element to the queue, it is inserted in a position based on its priority value. For example, if you add an element with a high priority value to a priority queue, it may be inserted near the front of the queue, while an element with a low priority value may be inserted near the back.

There are several ways to implement a priority queue, including using an __array, linked list, heap, or binary search tree__. Each method has its own advantages and disadvantages, and the best choice will depend on the specific needs of your application.

Priority queues are often used in real-time systems, where the order in which elements are processed can have significant consequences. They are also used in algorithms to improve their efficiencies, such as *Dijkstra’s algorithm* for finding the shortest path in a graph and the *A* search* algorithm for pathfinding.

# Properties

> priority queue is an extension of a queue
- Every item has a priority associated with it
- element with high priority is dequeued before an element with low priority
- If two elements have the same priority, they are served according to their order in the queue.

# Operations of a Priority Queue

1. Insertion
2. Deletion
3. Peek: This operation helps to return the maximum element from Max Heap or the minimum element from Min Heap without deleting the node from the priority queue.

# Types of a Priority Queue

1. Ascending order Priority Queue, or called as Min-heap for heap implementation
2. Descending order Priority Queue, or called as Max-heap for heap implementation

# Difference with a normal Queue
There is no priority attached to elements in a queue, the rule of __first-in-first-out(FIFO)__ is implemented whereas, in a priority queue, the 
elements have a priority. The elements with higher priority are served first.

# Applications of Priority Queue: 
CPU Scheduling
Graph algorithms like Dijkstra’s shortest path algorithm, Prim’s Minimum Spanning Tree, etc.
Stack Implementation
All queue applications where priority is involved.
Data compression in Huffman code
Event-driven simulation such as customers waiting in a queue.
Finding Kth largest/smallest element.

# Advantages of Priority Queue:
- It helps to access the elements in a faster way. This is because elements in a priority queue are ordered by priority, one can easily retrieve 
the highest priority element without having to search through the entire queue.
- The ordering of elements in a Priority Queue is done dynamically. Elements in a priority queue can have their priority values updated, which allows the queue to dynamically reorder itself as priorities change.
- Efficient algorithms can be implemented. Priority queues are used in many algorithms to improve their efficiency, such as Dijkstra’s algorithm for finding the shortest path in a graph and the A* search algorithm for pathfinding.
- Included in real-time systems. This is because priority queues allow you to quickly retrieve the highest priority element, they are often used in real-time systems where time is of the essence.

# Disadvantages of Priority Queue:
- High complexity. Priority queues are more complex than simple data structures like arrays and linked lists, and may be more difficult to implement and maintain.
- High consumption of memory. Storing the priority value for each element in a priority queue can take up additional memory, which may be a concern in systems with limited resources.
- It is not always the most efficient data structure. In some cases, other data structures like heaps or binary search trees may be more efficient for certain operations, such as finding the minimum or maximum element in the queue.
- At times it is less predictable:. This is because the order of elements in a priority queue is determined by their priority values, the order in 
which elements are retrieved may be less predictable than with other data structures like stacks or queues, which follow a first-in, first-out
(FIFO) or last-in, first-out (LIFO) order.

