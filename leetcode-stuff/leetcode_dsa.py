from typing import List
from collections import deque


# Binary search
def BinarySearch(arr:List[int], target:int) -> int:
    left, right = 0, len(arr) - 1
    first_true_index = -1

    while left <= right:
        mid = (left + right) // 2
        # overflow prevention: mid = left + (right - left) // 2

        if feasible(mid): # feasible means that the middle element serves one of the three conditions (equal, greater, less)
            first_true_index = mid
            right = mid + 1
        else:
            left = mid - 1
    return first_true_index

# Breadth-first Search
def level_order_traversal (root):

    if not root:
        return []
    
    result = []

    queue = deque([root])
    while len(queue) > 0:
        level = []

        for i in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

            # Given that we might need to do some operations for this level's list of values
            result.append(level)
        return result
    
# Tree Depth-first Search
def dfs(root, target):
    if root is None:
        return None
    
    if root.val == target:
        return root
    
    left = dfs(root.left, target)

    if left is not None:
        return left
    
    return dfs(root.right, target)

# Graph Depth-first search (cycles exist)

def GraphDFS(root, visited):
    for neighbor in get_neighbors(root):
        if neighbor in visited:
            continue
        
        visited.add(neighbor)
        dfs(neighbor, visited)

# An example of backtracking with combinations of keys on a phone
digit_to_char = {
    '2': 'abc', '3': 'def', '4':'ghi', '5': 'jkl',
    '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
}

def letterCombinations(digits):

    if not digits:
        return []
    
    ans = []

    def dfs(start_index, path):
        if start_index == len(digits):
            ans.append("".join(path))
            return
    
        for char in digit_to_char[digits[start_index]]:
            path.append(char)
            dfs(start_index+1, path)

            path.pop()
    
    dfs(0, [])

    return ans

# Dynamic Programming

