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
        current_city = path[i]
        next_city = path[i + 1]
        cost += graph[current_city].get(next_city, 0)  # Get the edge cost or 0 if the edge doesn't exist
    return cost

# Example usage:
if __name__ == "__main__":
    # Define the graph as a dictionary
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

    for city in start_cities:
        path = dfs(graph, city, goal_city)
        if path:
            cost = calculate_path_cost(graph, path)
            print("Path from {} to {}: {}.".format(city, goal_city, " -> ".join(path)))
            print("Total cost: {}".format(cost))
        else:
            print("No path found from {} to {}.".format(city, goal_city))

"""
    # Initial test
    start_city = "Arad"

    path = dfs(graph, start_city, goal_city)
    if path:
        print("Path from {} to {}: {}".format(start_city, goal_city, " -> ".join(path)))
    else:
        print("No path found from {} to {}.".format(start_city, goal_city))

"""