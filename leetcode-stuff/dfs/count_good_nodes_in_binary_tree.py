# PROBLEM 1448. Count Good Nodes in Binary Tree
# MEDIUM , Microsoft frequently asked interview questions

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # traverse the binary in dfs fashion
        # for every node check, if the previous node is not larger 
        # recursively call on the next node in the stack (stack for dfs)
        # NOTE: max value when tracing back to the root matters

        # initialize the number of good nodes to return
        # root node is always a good node (according to the problem)
        good_nodes = 1
        # Utility function - depth-first search to check for the subsequent nodes
        def dfs(node, maxVal):
            # The nonlocal keyword is used to work with variables inside nested functions, where the variable should not belong to the inner function.
            # reference: https://www.w3schools.com/python/ref_keyword_nonlocal.asp
            nonlocal good_nodes
            if node.left:
                if node.left.val >= maxVal:
                    good_nodes += 1
                dfs(node.left, max(maxVal, node.left.val))
            if node.right:
                if node.right.val >= maxVal:
                    good_nodes += 1
                dfs(node.right, max(maxVal, node.right.val))

        dfs(root, root.val)
        return good_nodes
        """
        # NEETCODE
        def dfs(node, maxVal):
            if not node:
                return 0
            
            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res
        return dfs(root, root.val)
        """