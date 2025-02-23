# LEETCODE 399. Evaluate Division
# This is supposed to be a breadth-first search solution, eventhough it was categorized as a dfs problem
import collections
from collections import deque
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        # for query in queries:
        # check for the numerator
        # 
        # check for the denominator

        # STEP 1:
        # Create an adjacency matrix
        adj = collections.defaultdict(list) # Map a -> list of [b, a/b]
        for i, equation in enumerate(equations):
            # unpack the pair of numerator-denominator
            a, b = equation
            # add the new nodes (pair of variables) and their connecting edges
            # which is the division value
            adj[a].append([b, values[i]])
            adj[b].append([a, 1/values[i]]) # the reverse direction b->a with the reciprocal

        # STEP 2: Run the breadth-first search algorithm after building the adjacency matrix accordingly
        # a / b, a -> b: run all instances from a that can lead to b
        def bfs(src, target):
            # given two variables that are not mentioned in the equations
            # return -1 like requested
            if src not in adj or target not in adj:
                return -1
            # q: a deque to work as a queue for our breadth-first search algorithm
            q, visit = deque(), set()
            # everytime we add the node to the queue
            # starting value with itself, so 1 is the current defaulted multiplicant
            q.append([src, 1])

            # add the visited variable to the set
            visit.add(src)
            while q:
                # pop out the next in a first-in-first-out order
                n, w = q.popleft()
                # if we reach the target variable, we can return the resulting w we have multiplied
                if n == target:
                    return w
                for neighbor, weight in adj[n]:
                    if neighbor not in visit:
                        q.append([neighbor, weight*w]) # we want to multipy the current weight 
                                                       # with the preceding product we have built with the previous nodes
                        visit.add(neighbor)
            # if all nodes visited but not found
            return -1
        return [bfs(q[0], q[1]) for q in queries]
