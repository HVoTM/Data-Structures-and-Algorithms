# LEETCODE 450. Delete Node from a Binary Search Tree
# Definition for a binary tree node.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        Reminder on Binary Search tree: left child has a smaller value while the right child has 
        a greater value than the node's value.
        """
        # https://www.youtube.com/watch?v=LFzAoJJt92M&ab_channel=NeetCodeIO
        # Base case 
        if root is None:
            return root
        
        # Search stage
        # adhering to BST properties, we continue to traverse along the right subtree to find the larger value
        # until we find the node value that is equal to key
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        # the other case
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        # if we found the key
        else:
            # these next 2 conditions check if there is a single child for the node we found
            # meaning return left child if right child is nonexistent and vice versa
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # this is for if there are both left and right child in the node that we found
            # Find the minimum from right subtree in order to preserve the value ordering
            # in the right subtree of a Binary Search Tree
            cur = root.right
            while cur.left:
                cur = cur.left 
            root.val  = cur.val
            # this step is to call for the 
            root.right = self.deleteNode(root.right, root.val)
        
        return root
        """
        def bfs(node):
            nonlocal key
            # Base case handling
            if node is None:
                return
            
            # if encountered the key value we were searching
            if node.val == key:
                return node.left, node.right

            left_search = bfs(node.left)
            right_search = bfs(node.right)

            if left_search:
                node.left = left_search[0]
                node.left.right = left_search[1]

            elif right_search:
                node.right = right_search[1]
                node.right.left = right_search[0]

        bfs(root)
        return root
        """