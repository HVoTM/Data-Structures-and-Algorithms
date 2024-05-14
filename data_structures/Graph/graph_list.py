# Implementation of graph using Adjacency List Representation

class Graph:
    def __init__(self):
        self.graph = {}
    
    def print_graph(self):
        for vertex in self.graph:
            print(vertex, '->', ' -> '.join(map(str, self.graph[vertex])))

# Examples of polymorphism
class UndirectedGraph(Graph):
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        
        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)
        self.graph[v].append(u) # For an undirected graph
        
class DirectedGraph(Graph):
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
        
# Create a graph and add edges
if __name__ == '__main__':

    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 3)

    # Print the graph
    g.print_graph()