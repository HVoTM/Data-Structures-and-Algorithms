# Kruskal's Algorithm Implemented (Greedy Algorithm)

# Minimum spanning tree: a minimum weighted spanning tree for a weighted, connected, undirected graph 
"""Method
1. Sort all the edges in non-decreasing order of their weight
2. union-find: Pick the smallest edge, check if form a cycle with the spanning tree formed so far
3. repeat #2 until there are V-1 edges 
"""

"""Kruskal's Algorithm on Wikipedia: https://en.wikipedia.org/wiki/Kruskal%27s_algorithm
algorithm Kruskal(G) is
    F:= ∅
    for each v in G.V do
        MAKE-SET(v)
    for each {u, v} in G.E ordered by weight({u, v}), increasing do
        if FIND-SET(u) ≠ FIND-SET(v) then
            F := F ∪ { {u, v} }
            UNION(FIND-SET(u), FIND-SET(v))
    return F
"""

class Graph: # graph data structure: weighted, undirected
    def __init__(self, num_vertices):
        self.v = num_vertices
        self.graph = [] # too flashy?, [] should suffice
        # TODO: add dictionary method later

        # Disjoint set data structure
        self.parent = list(range(self.v)) # initialize a list of parent nodes, which are the nodes themselves
        self.rank = [0] * self.v # set all ranks to 0, since we will be initializing a forest a single-vertex trees
    
    # data structure of a weighted, undirected graph
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])
        # TODO: feature to make sure the edge is undirected
        # TODO: feature to make sure new edge is not already in the graph

    # Inserting a new set
    def make_set(self, v):
        self.parent[v] = v
        self.rank[v] = 0

    # Determine which subset a particular element is in
    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        
        return self.parent[v]
    """Note:
    With the find and union method in Disjoint Sets, we can utilize their features to check if edges form a cycle
    As MST already completed, even if the algorithm continues to search for edge, it will always encounter
    the remaining edges to be forming a cycle, MST is preserved
    """
    # Join two subsets into a single subset
    def union(self, a, b): # Using Union by Rank

        root_a = self.find(a)
        root_b = self.find(b)

        if root_a != root_b:
            if self.rank[root_a] < self.rank[root_b]:
                self.parent[root_a] = root_b
            elif self.rank[root_a] > self.rank[root_b]:
                self.parent[root_b] = root_a
            else:
                self.parent[root_b] = root_a
                self.rank[root_a] += 1
    
    # Kruskal's algorithm implemented to find the minimum spanning tree
    # both for connected and disconnected weighted, undirected graphs 
    def kruskalMST(self):
        # store the resultant MST
        forest = []
        self.graph = sorted(self.graph, key=lambda item:item[2]) # NOTE: sorted() builtin function can work on iterables
        # https://docs.python.org/3/library/functions.html#sorted

        i = 0 # index variable used for the sorted edges
        e = 0 # implement a check flag to make sure E = V-1
        
        for node in range(self.v):
            self.make_set(node)

        while e < self.v - 1: # checking if MST is formed and completed to finish the algorithm
            # for optimization and efficiency in larger-scale implementation
            
            # Pick the smallest edge
            u, v, w = self.graph[i]
            i += 1
            x = self.find(u)
            y = self.find(v)

            # Check if two nodes' parents are the same -> form a cycle
            if x != y:
                e += 1
                forest.append([u, v, w])
                self.union(u, v)
            # else discard the edge - skip over the next edge
    
        minCost = 0
        print('Minimum Spanning Tree found with Kruskal\'s Algorithm:')
        for u, v, w in forest:
            minCost += w
            print("%d ---- %d == %d" % (u, v, w)) 
        
        print(f'Minimum Spanning Tree total weight cost: ', minCost)

# Driver code 
if __name__ == '__main__': 
    g = Graph(7) 
    g.add_edge(0, 1, 7) 
    g.add_edge(0, 3, 5)
    g.add_edge(1, 2, 8)
    g.add_edge(1, 3, 9)
    g.add_edge(1, 4, 7)
    g.add_edge(2, 4, 5)
    g.add_edge(3, 4, 15)
    g.add_edge(3, 5, 6)
    g.add_edge(4, 5, 8)
    g.add_edge(4, 6, 9)
    g.add_edge(5, 6, 11)
  
    # Function call 
    g.kruskalMST() 
  