# Implementation of Graph using Adjacency Matrix Representation

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, u, v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1  # For an undirected graph

    def print_graph(self):
        for row in self.graph:
            print(' '.join(map(str, row)))

# Create a graph of 4x4 and add edges
if __name__ == '__main__':
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 3)

    # Print the graph
    g.print_graph()
