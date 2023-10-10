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




