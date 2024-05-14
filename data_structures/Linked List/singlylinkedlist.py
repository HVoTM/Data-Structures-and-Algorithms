# Node class 
class Node: 

	# Function to initialize the node object 
	def __init__(self, data): 
		self.data = data # Assign data 
		self.next = None # Initialize next as null 

# Linked List class 


class LinkedList: 

	# Function to initialize the Linked List object 
	def __init__(self): 
		self.head = None

	def append(self, data):
		new_node = Node(data)
		if not self.head:
			self.head = new_node
		else:
			current = self.head
			while current.next:
				current=current.next
			current.next = new_node	

	def display(self):
		current = self.head
		while current:
			print(current.data, end = ' ')
			current = current.next
		print()

	# Iterative Approach to finding an element in the Linked list
	def search(self, x) -> bool:
		current = self.head
		while current: # Iterate over the list 
			if current.data == x:
				return True
			current = current.next
		return False
	
	# Recursive Approach to finding an element in the Linked List
	def search_cur(self, curr_node ,key) -> bool:
		if not curr_node:
			return False
		
		if curr_node.data == key:
			return True
		
		return self.search_cur(curr_node.next, key)

# Example usage:
slist = LinkedList()
slist.append(1)
slist.append(2)
slist.append(3)
slist.append(4)

print("The current Singly Linked List is:")
slist.display()  # Output: 1 2 3 4

inlist = slist.search(3)
if inlist:
	print('There is 3 in the Linked List')
else:
	print('There is not the corresponding value 3 in the list')

inlist = slist.search_cur(slist.head, 5)
if inlist:
	print('There is 5 in the Linked List')
else:
	print('There is not the corresponding value 5 in the list')
