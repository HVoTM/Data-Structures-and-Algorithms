from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # Intuition
        # if there is a sequential right node to the current left node, or left to the right node
        # traverse and continue counting
        # recursively call and compare with the current longest zig zag length

        # Helper function to perform DFS (depth-first search) on the tree
        def dfs(node: Optional[TreeNode], left_length, right_length):
            # left_length and right_length represents the length of the current zig zag path in that node
            # if there is a continuing left node, we want to update the left_length by right_length + 1
            # and reset the right_length since we want to keep track if we are on a zig zag track or not
            # This is because a move to the left child is seen as a previous right move from the parent node's perspective.
            # vice versa for right node traversal
            # base case of empty node, end of the depth of binary tree branch
            if node is None:
                return
            # Update the global (nonlocal) parameter
            nonlocal max_length
            max_length = max(max_length, left_length, right_length)
            # Recursively explore the left child, incrementing the "left_length" as we are
            # making a zig (left direction) from the right side of the current node
            dfs(node.left, right_length + 1, 0)
            # Recursively explore the right child, incrementing the "right_length" as we are
            # making a zag (right direction) from the left side of the current node
            dfs(node.right, 0, left_length + 1)

        # Initialize the maximum length to 0 before starting DFS
        max_length = 0
        # Start DFS with the root of the tree, initial lengths are 0 as starting point
        dfs(root, 0, 0)
        # Once DFS is complete, return the maximum zigzag length found
        return max_length
