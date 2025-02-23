# LEETCODE 235. Lowest Common Ancestor of a Binary Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # https://algo.monster/liteproblems/236
        # If the root is None, or the root is one of the nodes we're looking for,
        # we return the root as the LCA (Lowest Common Ancestor)
        if root is None or root == p or root == q:
            return root

        # Look for the LCA in the left subtree
        left_lca = self.lowestCommonAncestor(root.left, p, q)

        # Look for the LCA in the right subtree
        right_lca = self.lowestCommonAncestor(root.right, p, q)

        # If both left and right LCA are non-null, it means one node is in the left
        # subtree and the other is in the right, so root is the LCA
        if left_lca and right_lca:
            return root

        # Otherwise, if one of the LCAs is non-null, return that one
        return left_lca if left_lca else right_lca