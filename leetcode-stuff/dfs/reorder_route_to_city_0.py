from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # Start at city 0
        # recursively check for its neighbors
        # count outgoing edges

        # Create a set for existing edges between the nodes for cross-examination in dfs()
        # since set is an unordered data structure type, which proves to be useful later
        edges = {(a, b) for a, b in connections}
        # create a hash map for every city's neighbors that we can add to the
        # n: n cities - n routes
        neighbors = {city: [] for city in range(n)}
        # Create a set structure to store visited city during the recursive search of dfs()
        visit = set()
        # element to keep count of changes that need to be made for rerouting to 0 
        changes = 0
        # Initiate over all connections to create the hashmap for information storage
        for a, b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)
        # Utility function to perform depth-first search for each city 
        def dfs(city):
            # use nonlocal variable so that we do not need to pass them in every call
            nonlocal edges, neighbors, visit, changes

            for neighbor in neighbors[city]:
                if neighbor in visit:
                    continue
                # Check if this neighbor can reach city 0
                # unordered property in set works for check
                # if there is a route that can lead back to 0 -> pass
                # if there is not a route -> make changes and continue to the next neighbor
                # for dfs()
                if (neighbor, city) not in edges:
                    changes += 1
                visit.add(neighbor)
                # Recursively run on the next neighbors
                dfs(neighbor)
        visit.add(0)
        dfs(0)
        return changes
