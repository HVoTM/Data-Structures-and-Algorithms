# Python program to introduce Binary Tree

# A class that represents an individual node
# in a Binary Tree
class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.key = key

# Class to implement Binary Trees
class BinaryTree:
	def __init__(self):
		self.root = None
	
	def insert(self, data):
		self.root = self.insert_rec(self.root, data)
	
	def insert_rec(self, root, data):
		if root is None:
			return Node(data)
		
		if data < root.key:
			root.left = self.insert_rec(root.left, data)
		else:
			root.right = self.insert_rec(root.right, data)
		return root
	
	def delete(self, key):
		self.root = self._delete_rec(self.root, key)

	def _delete_rec(self, root, key):
		if root is None:
			return root

		if key < root.key:
			root.left = self._delete_rec(root.left, key)
		elif key > root.key:
			root.right = self._delete_rec(root.right, key)
		else:
            # Node with only one child or no child
			if root.left is None:
				return root.right
			elif root.right is None:
				return root.left

            # Node with two children: find the in-order successor (smallest in the right subtree)
			root.key = self._min_value_node(root.right).key
			root.right = self._delete_rec(root.right, root.key)

		return root

	def _min_value_node(self, node):
		while node.left is not None:
			node = node.left	
		return node

	# Implementing traversal of all three kinds: inorder, preorder, postorder using recursion
	def inorder_traversal(self):
		result = []
		self._inorder_rec(self.root, result)
		return result

	# Inorder traversal: 
	# Traverse the left subtree(call Inorder)	
	# Visit the root
	# Traverse the right subtree (call Inorder)
	def _inorder_rec(self, root, result):
		if root:
			self._inorder_rec(root.left, result)
			result.append(root.key)
			self._inorder_rec(root.right, result)

	def preorder_traversal(self):
		result = []
		self.preorder_rec(self.root, result)
		return result
	
	# Here, in the preorder method: 
	# Visit the root
	# Traverse the left subtree (call Preorder)
	# Then traverse the right subtree (call Preorder)
	def preorder_rec(self, root, result):
		if root:
			result.append(root.key)
			self.preorder_rec(root.left, result)
			self.preorder_rec(root.right, result)
	
	def postorder_traversal(self):
		result = []
		self._postorder_rec(self.root, result)
		return result

	# Here, in the postorder method:
	# Traverse the left subtree (call Postorder)
	# Traverse the right subtree (call Postorder)
	# Visit the root
	def _postorder_rec(self, root, result):
		if root:
			self._postorder_rec(root.left, result)
			self._postorder_rec(root.right, result)
			result.append(root.key)


# Driver code
if __name__ == '__main__':
	bt = BinaryTree()
	bt.insert(50)
	bt.insert(30)
	bt.insert(70)
	bt.insert(20)
	bt.insert(40)

	print("Inorder Traversal:", bt.inorder_traversal())  # Output: [20, 30, 40, 50, 70]
	print("Preorder Traversal:", bt.preorder_traversal())  # Output: [50, 30, 20, 40, 70]
	print("Postorder Traversal:", bt.postorder_traversal())  # Output: [20, 40, 30, 70, 50]

	bt.delete(30)
	print("After deleting 30:", bt.inorder_traversal())  # Output: [20, 40, 50, 70]