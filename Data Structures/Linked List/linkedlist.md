# Definition

Linked List is a linear data structure, in which elements are not stored at a contiguous location, rather they are linked using pointers. Linked List forms a series of connected nodes, where each node stores the data and the address of the next node.  

- Node Structure: A node in a linked list typically consists of two components:
    - Data: It holds the actual value or data associated with the node.
    - Next Pointer: It stores the memory address (reference) of the next node in the sequence.
- Head and Tail: The linked list is accessed through the head node, which points to the first node in the list. The last node in the list points 
to NULL or nullptr, indicating the end of the list. This node is known as the tail node.

# Advantages:
- __Dynamic Data structure__: The size of memory can be allocated or de-allocated at run time based on the operation insertion or deletion.
- __Ease of Insertion/Deletion__: The insertion and deletion of elements are simpler than arrays since no elements need to be shifted after
insertion 
and deletion, Just the address needed to be updated.
- __Efficient Memory Utilization__: As we know Linked List is a dynamic data structure the size increases or decreases as per the requirement so this avoids the wastage of memory. 
- __Implementation__: Various advanced data structures can be implemented using a linked list like a stack, queue, graph, hash maps, etc.

# Types of Linked lists:

There are mainly three types of linked lists:

1. Single-linked list
2. Double linked list
3. Circular linked list

# Operations on Linked Lists:

Operations on Linked Lists
- __Insertion__: Adding a new node to a linked list involves adjusting the pointers of the existing nodes to maintain the proper sequence.
Insertion can be performed at the beginning, end, or any position within the list
- __Deletion__: Removing a node from a linked list requires adjusting the pointers of the neighboring nodes to bridge the gap left by the deleted 
node. Deletion can be performed at the beginning, end, or any position within the list.
- __Searching__: Searching for a specific value in a linked list involves traversing the list from the head node until the value is found or the end of the list is reached.