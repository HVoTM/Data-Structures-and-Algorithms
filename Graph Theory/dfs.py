"""
Depth-First Search
Algorithm used to search a graph data structure for a node that meets a set of critera.
It starts at the root of the graph and visits all nodes at the current depth level 
before moving on to the nodes at the next depth level.

- A boolean visited array is used to mark the visited vertice (assuming all vertices are reachable from
the starting vertex)
- Uses a stack for traversal - LIFO
- Adjacency list for graph representation

"""
from collections import defaultdict # further info: https://docs.python.org/3/library/collections.html#defaultdict-objects
# one main advantage when using defaultdict is that when trying to look up
# a key it does not contain, it first adds a value for it using zero-argument function
# The class represents a directed graph using adjacency list representation
from collections import deque

class Graph:
    # Constructor
    def __init__(self) -> None:
        # initialize a defaultdict using a list -> a dictionary of list
        self.graph = defaultdict(list) # now we have a dictionary of keys being the node
                                       # and items being the lists of adjacent nodes, also we 
                                       # can use append() and other list methods to play around
    
    # function to add an edge between two vertices
    def addEdge(self, u, v) -> None:
        self.graph[u].append(v)
        # if undirected graphs, add: self.graph[v].append(u)

    # Depth-first search algorithm
    def dfs(self, s) -> None: # s being the root node to traverse/search
        # Mark all vertices as not visited in the boolean list
        visited = [False] * len(self.graph)
        
        # create a queue for BFS
        stack = deque()
        
        # Given that s is the first visited, add to queue for search
        visited[s] = True
        stack.append(s) # NOTE: LIFO - adding gradually from the left 
        
        while stack: # check while queue is not empty
            
            # Dequeue a vertex from q
            s = stack.pop() # NOTE: LIFO - pop the first one on the right
            print(s, end=" ")
            
            # Get adjacent vertices of the currently dequeued vertex
            # If one of the vertices has not been visited, mark as visited and append into queue
            for i in self.graph[s]:
                if visited[i] == False:
                    stack.append(i)
                    visited[i] = True
        
        """Notes on implementing stack(or even queue)
        We can use deque(), a Python's collections object: https://docs.python.org/3/library/collections.html#deque-objects
        import collections as deque
        
        stack = deque()
        
        # For Depth-First Search, we will do Last-In First-Out method
        stack.appendleft(v) # vertices pushed in from the left
        stack.pop() # to pop the lastest element in, which is at the right
        """
# Driver's code
if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
 
    print("Following is Depth First Traversal (starting from vertex 2)")
     
    # Function call
    g.dfs(2)