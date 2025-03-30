"""Dijkstra's Algorithm

Find the shortest paths from the source vertex to all other vertices in the graph. Iteratively selecting the 
vertex with the minimum distance from the source vertex and updating the distances to its neighboring vertices
Characteristics:
- The graph only contain non-negative edge weights
- Greedy method
- works with directed and undirected graphs

Overview:
- Maintain a 'dist' array where the distance to every node is positive infinity. Distance of start node is 0
- Maintain a priority queue of key-value pairs (node, index, distance) to tell which node to visit next based on sorted min p.queue
- Insert (s,0) into the priority queue and loop while pq is not empty puling out the next most promising pair
- Iterate over all edges outwards from the current node and relax each edge appending a new key-value pair to the pq 
"""
from collections import defaultdict
import heapq # heapq will be using min-heap properties

class DiGraph():
    def __init__(self) -> None:
        self.graph = defaultdict(dict)
    
    # function to add edge and weight 
    def add_edge_weight(self, u: int, v: int, w: int) -> None:
        self.graph[u].update({v: w})
    
    # TODO: fix the output display, so that it can show the weight of the edges
    def print_graph(self):
        for vertex in self.graph:
            print(vertex, '->', ' -> '.join(map(str, self.graph[vertex])))
    
    def dijkstra(self, start: int, num_vertices: int) -> None:
        visited = [False] * num_vertices
        dist = [float('inf')] * num_vertices # list of distances to all vertices set to positive infinity initially
        dist[start] = 0 # initiallize the starting vertex with distance value 0
        # initialize a priority queue for the algorithm
        pq = [(start, 0)] # (vertex, distance)
        
        while pq:
            # Get the vertex with the minimum distance
            current_vertex, current_dist = heapq.heappop(pq)
            
            # Ignore vertices that have been visited
            if current_dist > dist[current_vertex]:
                continue
            
            # Visit each neighbor of the current vertex
            for neighbor, weight in self.graph[current_vertex].items():
                distance = current_dist + weight
                # Update the distance if a shorter path is found
                if distance < dist[neighbor]:
                    dist[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
            
            return dist
            
# Test drive
if __name__ == "__main__":
    dg = DiGraph()
    dg.add_edge_weight(0, 2, 3)
    dg.add_edge_weight(0, 1, 5)
    dg.add_edge_weight(1, 4, 3)
    dg.add_edge_weight(1, 3, 2)
    dg.add_edge_weight(2, 4, 1)
    dg.add_edge_weight(3, 0, 5)
    dg.print_graph()
    #