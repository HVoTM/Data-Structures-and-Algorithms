# Prim's Algorithm for Minimum Spanning Tree (Greedy Algorithm)

# Minimum spanning tree: a minimum weighted spanning tree for a weighted, connected, undirected graph 
# NOTE: main difference with kruskal is that prim works on
# DISCONNECT graphs

"""Method
1. Determine an arbitray vertex as the starting vertex of MST
    - Basically we have two subsets of vertices: MST's included vertices and fringe vertices
    - They can be considered disjoint subsets of the tree
2. Find edges connecting the tree vertices with the fringe vertices
    - Find the minimum weight among these edges
    - The minimum weight edge cannot form a cycle
    - Add the edge and corresponding ending vertex to the MST
3. Repeat 2 until all fringe vertices are added
4. Return MST
"""

"""Cut(Graph theory)
- Group of edges that connect two sets of vertices in a graph
"""
import numpy as np # using numpy arrays for faster memory
class Graph: # undirected, weighted graph ds
    def __init__(self, num_vertices) -> None:
        self.v = num_vertices
        # We will try with adjacency matrix representation
        self.graph = np.zeros((num_vertices, num_vertices), dtype=int)
        
    def add_edge(self, u, v, w) -> None:
        self.graph[u, v] = w
        self.graph[v, u] = w

    def print_graph(self) -> None:
        print(self.graph)
    
    # Prim's algorithm utility function to find the minimum weight of the cuts
    def min_weight(self, u, v):
        pass

    # Function to construct and print MST for a graph
    def prim_mst(self, u: int): 
        mst = []



if __name__ == '__main__':
    g = Graph(5)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 4, 8)
    g.add_edge(1, 3, 9)
    g.add_edge(2, 3, 7)
    g.print_graph()