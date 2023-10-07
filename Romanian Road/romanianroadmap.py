# HOMEWORK 2: DEPTH SEARCH, BREADTH SEARCH, A* SEARCH
# NAME: Hung Vo, Khoa Dang
from collections import deque
import heapq

def astar(graph, start, goal, heuristic):
    # Create a priority queue for A* search
    open_list = [(0, start)]
    
    # Create dictionaries to store g-scores and parents
    g_scores = {city: float('inf') for city in graph}
    g_scores[start] = 0
    parents = {}
    
    while open_list:
        # Pop the city with the lowest f-score
        current_f, current_city = heapq.heappop(open_list)
        
        # Check if the goal city is reached
        if current_city == goal:
            path = []
            while current_city:
                path.append(current_city)
                current_city = parents.get(current_city)
            return list(reversed(path))
        
        for neighbor in graph[current_city]:
            # Calculate tentative g-score
            tentative_g = g_scores[current_city] + graph[current_city][neighbor]
            
            if tentative_g < g_scores[neighbor]:
                # This is a better path, update g-score and parent
                g_scores[neighbor] = tentative_g
                f_score = tentative_g + heuristic[neighbor]
                heapq.heappush(open_list, (f_score, neighbor))
                parents[neighbor] = current_city
    
    # If no path is found, return an empty list
    return []

def bfs(graph, start, goal):
    # Create a queue for BFS
    queue = deque()
    
    # Create a set to keep track of visited cities
    visited = set()
    
    # Initialize the queue with the starting city and an empty path
    queue.append((start, []))
    
    while queue:
        # Dequeue the current city and its path
        current_city, path = queue.popleft()
        
        # Mark the current city as visited
        visited.add(current_city)
        
        # Check if the goal city is reached
        if current_city == goal:
            return path + [current_city]
        
        # Explore neighboring cities
        for neighbor in graph[current_city]:
            if neighbor not in visited:
                # Enqueue the neighbor and update the path
                queue.append((neighbor, path + [current_city]))
    
    # If no path is found, return an empty list
    return []

def dfs(graph, start, goal):
    # Create a stack for DFS
    stack = [(start, [])]
    
    # Create a set to keep track of visited cities
    visited = set()
    
    while stack:
        # Pop the current city and its path
        current_city, path = stack.pop()
        
        # Mark the current city as visited
        visited.add(current_city)
        
        # Check if the goal city is reached
        if current_city == goal:
            return path + [current_city]
        
        # Explore neighboring cities in reverse order
        for neighbor in reversed(graph[current_city]):
            if neighbor not in visited:
                # Push the neighbor and update the path
                stack.append((neighbor, path + [current_city]))
    
    # If no path is found, return an empty list
    return []

def calculate_path_cost(graph, path):
    cost = 0
    for i in range(len(path) - 1):
        cost += graph[path[i]][path[i + 1]]
    return cost

# Example usage:
if __name__ == "__main__":
    # Define the graph as a dictionary with edge costs
    graph = {
        "Arad": {"Zerind": 75, "Sibiu": 140, "Timisoara": 118},
        "Zerind": {"Arad": 75, "Oradea": 71},
        "Oradea": {"Zerind": 71, "Sibiu": 151},
        "Sibiu": {"Arad": 140, "Oradea": 151, "Fagaras": 99, "Rimnicu Vilcea": 80},
        "Timisoara": {"Arad": 118, "Lugoj": 111},
        "Lugoj": {"Timisoara": 111, "Mehadia": 70},
        "Mehadia": {"Lugoj": 70, "Drobeta": 75},
        "Drobeta": {"Mehadia": 75, "Craiova": 120},
        "Craiova": {"Drobeta": 120, "Rimnicu Vilcea": 146, "Pitesti": 138},
        "Rimnicu Vilcea": {"Sibiu": 80, "Craiova": 146, "Pitesti": 97},
        "Fagaras": {"Sibiu": 99, "Bucharest": 211},
        "Pitesti": {"Rimnicu Vilcea": 97, "Craiova": 138, "Bucharest": 101},
        "Bucharest": {"Fagaras": 211, "Pitesti": 101},
        "Giurgiu" :{"Bucharest": 90},
        "Urziceni" : {"Bucharest" : 85, "Vaslui": 142, "Hirsova": 98},
        "Hirsova": {"Urziceni": 98, "Eforie": 86},
        "Eforie" : {"Hirsova": 86},
        "Vaslui" : {"Urziceni": 142, "Iasi": 92},
        "Iasi" : {"Vaslui" : 92, "Neamt": 87},
        "Neamt" : {"Iasi": 87},
    }

    start_cities = ["Neamt", "Oradea", "Timisoara"]
    goal_city = "Bucharest"

    # Define a heuristic function (straight-line distance to Bucharest)
    heuristic = {
        "Arad": 366,
        "Zerind": 374,
        "Oradea": 380,
        "Sibiu": 253,
        "Timisoara": 329,
        "Lugoj": 244,
        "Mehadia": 241,
        "Drobeta": 242,
        "Craiova": 160,
        "Rimnicu Vilcea": 193,
        "Fagaras": 178,
        "Pitesti": 98,
        "Bucharest": 0,
        "Urziceni": 80,
        "Hirsova" : 151,
        "Eforie" : 161,
        "Vaslui" : 199,
        "Iasi" : 226,
        "Neamt" : 234,
    }
    for city in start_cities:
        path = astar(graph, city, goal_city, heuristic)
        if path:
            print("A* Search: Path from {} to {}: {}".format(city, goal_city, " -> ".join(path)))
            total_cost = calculate_path_cost(graph, path)
            print("Total cost: {}".format(total_cost))
        else:
            print("No path found from {} to {}.".format(city, goal_city))

        path = bfs(graph, city, goal_city)
        if path:
            cost = calculate_path_cost(graph, path)
            print("Breadth-First Search: Path from {} to {}: {}.".format(city, goal_city, " -> ".join(path)))
            print("Total cost: {}".format(cost))
        else:
            print("No path found from {} to {}.".format(city, goal_city))

        path = dfs(graph, city, goal_city)
        if path:
            cost = calculate_path_cost(graph, path)
            print("Depth-First Search: Path from {} to {}: {}.".format(city, goal_city, " -> ".join(path)))
            print("Total cost: {}".format(cost))
        else:
            print("No path found from {} to {}.".format(city, goal_city))