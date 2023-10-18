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

	# INSERTION
	# Function to insert a new node at the beginning
	def push(self, new_data):
		
		# Allocate the node and assign data
		new_node = Node(new_data)

		# Make the next of New node as head
		new_node.next = self.head

		# Move the head to point to new Node
		self.head = new_node

	# Function to insert a new node after a give prev_node
	def InsertAfter(self, prev_node, new_data):
		# Check if the prev_node exists

		if prev_node is None:
			print("The given previous node must be in Linkedlist, this one is not")
			return
		
		# Create a new node and assign data
		new_node = Node(new_data)

		# Make the next of the new_node as the next of the prev_node
		new_node.next = prev_node.next

		# make the next of the prev_node as the new_node
		prev_node.next = new_node

	# Function to insert node at the end
	def append(self, new_data):
		# Create a new node and assign data
		new_node = Node(new_data)

		# if Linkedlist is empty, make the new node as head
		if self.head is None:
			self.head = new_node
			return
		
		# Traverse till the last node
		last = self.head
		while(last.next):
			last = last.next

		# Change the next of last node to new_node
		last.next = new_node