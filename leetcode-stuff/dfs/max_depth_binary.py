# LEETCODE 104. Maximum Depth of a Binary Tree
# Depth-First Search

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def Solution1(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            # if there is a node (root node, specifically)
            # height is now 1
            # we recursively call on the children nodes until no more nodes are present
            # return and add from the bottom up

            left_depth = self.Solution1(root.left)
            right_depth = self.Solution2(root.right)

            if left_depth > right_depth:
                return left_depth + 1
            # We should have added another if-else statement for clarity on the case of equal depth on both right and left subtrees
            # but this should suffice as it is the same as returning left_depth + 1
            else:
                return right_depth + 1
            
    def Solution2(self, root: Optional[TreeNode]) -> int:
        def dfs(node, curr_depth):
            if node is None:
                return curr_depth

            leftsearch = dfs(node.left, curr_depth + 1)
            rightsearch = dfs(node.right, curr_depth + 1)
            return max(leftsearch, rightsearch)

        return dfs(root, 0)