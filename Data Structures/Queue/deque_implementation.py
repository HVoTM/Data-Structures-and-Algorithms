# Creating an empty queue, a structure to represent a queue
# With Queue, it would usually implement a First-in, First-out policy
# Here we are using deque (Double-ended queue, pronounced "deck")

# One of the reasons we use deque because it is efficient, supports thread-safe, memory efficient appends 
# and pops from either side of the deque with the euquivocal O(1) performance.

from collections import deque

queue = deque() # Initialize a deque

# Use append so we set the queue starting from the left to right

queue.append('j')
queue.append('a')
queue.append('r')
queue.append('v')

for element in queue:
    print(element)

# for FIFO policy, we use popleft, to remove from the left
print('Last item removed: ', queue[0])
queue.popleft()
print('Last item removed: ', queue[0])
queue.popleft()

# Notes: we can do an inverse method, appendleft to put on the left side, the pop from the right using pop
# like this:

"""
queue.appendleft('a')
queue.pop()
"""
queue.append('f')

# To show the leftmost and rightmost item, use d[0], d[-1]
print('The first element in the array: ', queue[0])
print('The last element in the array: ', queue[-1])
