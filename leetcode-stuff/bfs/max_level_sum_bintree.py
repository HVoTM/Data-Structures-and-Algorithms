from collections import deque
from math import inf
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 1

        # Initiate a queue data structure to perform the BFS search
        queue = deque([root])

        # mark the current level and the total visited nodes as we traverse the tree
        max_sum = -inf
        # initalize the level counter to 0
        level = 0
        # Initialize the answer to store the level with the maximum sum
        answer = 0

        # Traverse the tree in a breadth-first search order
        while queue:
            level += 1
            current_sum = 0
            # Process all the nodes at the current level
            # 1. add to the current sum of that current level
            # 2. for each node, we explore its children nodes to store for the next level
            for _ in range(len(queue)):
                # pop the leftmost node in the stack order property
                node = queue.popleft()
                # Add the node's value to the current level's sum
                current_sum += node.val
                # if the node has a left child
                if node.left:
                    queue.append(node.left)
                # same goes for right
                if node.right:
                    queue.append(node.right)
            
            # Update maximum sum and answer if the current level's sum is greater 
            # than max_sum
            if max_sum < current_sum:
                max_sum = current_sum
                answer = level
        return answer            

            
        