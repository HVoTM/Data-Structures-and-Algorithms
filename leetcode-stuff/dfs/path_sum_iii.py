from collections import Counter
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # Helper function to perform depth-first search
        def dfs(node, current_sum):
            # Base case
            if node is None:
                return 0

            # Increment the current path's sum with the current node's value
            current_sum += node.val

            # Number of times (current_sum - targetSum) has occured so far
            # which indicates a valid path when subtracting from the current_sum
            # any prior current_sum added to the path_count reoccurs will indicate 
            # there is a path that sum to the target value
            path_count = path_counts[current_sum - targetSum]

            # Store the current path's sum in the counter
            path_counts[current_sum] += 1

            # Recursively find paths in the left and right subtrees
            path_count += dfs(node.left, current_sum)
            path_count += dfs(node.right, current_sum)

            # Once the node is done, remove its sum from the counter
            # to not use it in the parallel subtree calls
            path_counts[current_sum] -= 1

            # Return the number of paths found
            return path_count
        
        # initialize a counter to keep track of all path sums
        path_counts = Counter({0: 1}) # starting from the root with an inital sum of 0

        return dfs(root, 0)
        # Time complexity: O(N), Space complexity: O(N)
        # Further explanation on the path_count
        # Path_counts will be used to count the number of occurences of a path sum, which usually stem from the root
        # As we progress downward on the branches, we keep up with checking the current_sum of the current node subtracted by the targetSum. 
        # If we have come across that path sum already, that means there is a path (can start from the root or in the middle of the tree)
        # that will satisfy the targetSum
        # be careful as we progress between the two sides of the tree since we need to 
        # decrement the prefix sum counts to prevent the current path's sum from affecting other paths as we --backtrack-- up the tree
"""
# Failed Attempt
        # Initialize the value to return
        correct_paths = 0
        # Utility function 
        def dfs(node):
            nonlocal targetSum, correct_paths
            # Base case
            if node is None:
                return 0
            # 
            # check with the target sum
            if ((node.val + dfs(node.left)) == targetSum) or ((node.val + dfs(node.right)) == targetSum):
                correct_paths += 1
            # Call on the next node to check
            sum_left = dfs(node.left)
            sum_right = dfs(node.right)
            return node.val

        # Evoke the recursive function to perform dfs over the tree
        dfs(root)

        return correct_paths
"""