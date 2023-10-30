# Node of a doubly linked list 
class Node: 
	def __init__(self, next=None, prev=None, data=None): 
		self.next = next # reference to next node in DLL 
		self.prev = prev # reference to previous node in DLL 
		self.data = data 

class DoublyLinkedList: 

	# Function to initialize the Linked List object 
	def __init__(self): 
		self.head = None

	# Create a new node in the linked list and add to the end of the list
	def append(self, data) -> None:
		new_node = Node(data)
		# Check if self.head is None
		if not self.head:
			self.head = new_node
		
		else:
			current = self.head
			# Check whether or not if the current node has a valid 'next' node
			while current.next:
				current = current.next
			current.next = new_node
			new_node.prev = current

	def display_forward(self):
		current = self.head
		while current:
			print(current.data, end =" ")
			current = current.next
		print()

	def display_backward(self):
		current = self.head
		while current and current.next:
			current = current.next

		while current:
			print(current.data, end = ' ')
			current = current.prev
		print()

# Example usage:
dlist = DoublyLinkedList()
dlist.append(1)
dlist.append(2)
dlist.append(3)
dlist.append(4)

print("Doubly Linked List (forward):")
dlist.display_forward()  # Output: 1 2 3 4

print("Doubly Linked List (backward):")
dlist.display_backward()  # Output: 4 3 2 1