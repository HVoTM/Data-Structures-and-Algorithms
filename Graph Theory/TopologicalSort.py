"""Topological Sort
Model a graph with directed edges where some events must occur before others (ordering of nodes)
- School class prerequisites
- Program dependencies
- Event scheduling
- Assembly Instructions

Find a topological ordering in O(|V|+|E|) time

Directed Acyclic Graphs (DAGs): graphs with directed edges and no cycles

# Algorithm:
Pick an unvisited node (arbitrary)
Do a Depth First Search exploring unvisited nodes. On recursive callback of the DFS, add the current node 
to the topological ordering in reverse order

In simpler term, it means that for the current vertex, we will check to see if there is an out-tree with that node as a root
Mark the traversed nodes as visited
Add the vertices from the last ones (the leaf nodes) first back to the root.
Recursively call on the all the nodes until they are all visited
Now we got a stack of nodes with the roots, or the ones with no in-degree at the last of the array
and the subsequent adjacent nodes back to the first of array.
That is why it is called DFS on all nodes' outputs in reverse order.

Applications of Topological Sorting:
Topological Sorting is mainly used for scheduling jobs from the given dependencies among jobs. 
In computer science, applications of this type arise in:
- Instruction scheduling
- Ordering of formula cell evaluation when recomputing formula values in spreadsheets
- Logic synthesis
- Determining the order of compilation tasks to perform in make files
- Data serialization
- Resolving symbol dependencies in linkers
"""
from collections import defaultdict

class Graph:
    def __init__(self, vertices: int):
        self.graph = defaultdict(list)
        self.vertices = vertices
    
    # destructor to unload an object of that class
    def __delattr__(self):
        pass
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        """USEFUL NOTE: 
        Using defaultdict will shorten the process, since it will create a key-item value if no value is found
        """
        # Check if the directed node (the one with the in-degree) has a slot in the graph yet
        # Since the above graph will take in the keys of the nodes pointing out
        # make sure to check if the other nodes are set in or not
        if v not in self.graph:
            self.graph[v] = []
        
        # check if we add more nodes than initial settings
        if len(self.graph) > self.vertices:
            self.vertices = len(self.graph)
    
    # function to check the graph visually       
    def print_graph(self):
        for vertex in self.graph:
            print(vertex, '->', ' -> '.join(map(str, self.graph[vertex])))

    # function to check if the graph is a DAG       
    def isCyclicUtil(self, v, visited, recStack):
 
        # Mark current node as visited and
        # adds to recursion stack
        visited[v] = True
        recStack[v] = True
 
        # Recur for all neighbours if any neighbour is visited and in recStack then graph is cyclic
        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True
 
        # The node needs to be popped from
        # recursion stack before function ends
        recStack[v] = False
        return False
 
    # Returns true if graph is cyclic else false
    def isCyclic(self):
        visited = [False] * (self.vertices + 1) 
        recStack = [False] * (self.vertices + 1)
        
        for node in range(self.vertices): # iterate over the vertices in the graph
            if visited[node] == False:
                if self.isCyclicUtil(node, visited, recStack) == True:
                    return True
        return False
                    
    # A recursive function used by topologicalSort
    def topologicalSortUtil(self, v, visited, stack):
 
        # Mark the current node as visited.
        visited[v] = True
 
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]: # seek out all the vertices that this current vertex points towards
            if visited[i] == False: # checks if they are visited yet
                self.topologicalSortUtil(i, visited, stack) # if not, recursive call on that node
 
        # Push current vertex to stack which stores result
        stack.append(v)
 
    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
    def topologicalsort(self):
        # Mark all the vertices as not visited
        visited = [False]* self.vertices
        # Array to store the visited nodes 
        stack = []
 
        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.vertices):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
 
        # Print contents of the stack
        print(stack[::-1])  # return list in reverse order

# Driver code
if __name__ == "__main__":
    g = Graph(6) # initialize with 6 vertices
    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)
    g.add_edge(7, 3) # we are adding more than 6 
    g.add_edge(6, 3)
    g.add_edge(4, 5)
    g.add_edge(2, 7)
    g.print_graph()
    g.topologicalsort()