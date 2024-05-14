# Definition

A stack is a linear data structure that stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner. In stack, a new element is added at one end and an element is removed from that end only. The insert and delete operations are often called push and pop.

The functions associated with stack are:

+ empty() – Returns whether the stack is empty – Time Complexity: O(1)
+ size() – Returns the size of the stack – Time Complexity: O(1)
+ top() / peek() – Returns a reference to the topmost element of the stack – Time Complexity: O(1)
+ push(a) – Inserts the element ‘a’ at the top of the stack – Time Complexity: O(1)
+ pop() – Deletes the topmost element of the stack – Time Complexity: O(1)

# Implementation:

There are various ways from which a stack can be implemented in Python. This article covers the implementation of a stack using data structures and modules from the Python library. 
Stack in Python can be implemented using the following ways: 

+ list
+ Collections.deque
+ queue.LifoQueue

# Advantages of Stack:

+ Stacks are simple data structures with a well-defined set of operations, which makes them easy to understand and use.
+ Stacks are efficient for adding and removing elements, as these operations have a time complexity of O(1).
+ In order to reverse the order of elements we use the stack data structure.
+ Stacks can be used to implement undo/redo functions in applications.

# Drawbacks of Stack:

+ Restriction of size in Stack is a drawback and if they are full, you cannot add any more elements to the stack.
+ Stacks do not provide fast access to elements other than the top element.
+ Stacks do not support efficient searching, as you have to pop elements one by one until you find the element you are looking for.