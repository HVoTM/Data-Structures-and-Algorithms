#include <vector>
#include <cstring>
#include <functional>

class Solution {

    public:
        int findCircleNum(std::vector<std::vector<int>>& isConnected) // note: & is used for referencing for saving and update
        {
            // Get the number of cities(nodes)
            int num_cities = isConnected.size();

            // Initialize the count of provinces
            int province_count = 0;

            // Initialize the visited array to keep track of the visited cities for the sequence of iterations
            bool visited[num_cities]; // reminder: been too long, this is an array
            // the reason we are also including vector library since vector has more functions to use

            // Initialize all cities as unvisited.
            std::memset(visited, false, sizeof(visited));

            // Define the depth-first search algorithm (DFS) as a lambda function
            std::function<void(int)> dfs = [&](int cityIndex){
                // Mark the current city as visited 
                visited[cityIndex] = true;

                // Visit all the unvisited cities if there is a connnection to that city with city of cityIndex
                for (int j=0; j< num_cities; j++){
                    if (!visited[j] && isConnected[cityIndex][j]){
                        dfs(j);
                    }
                }
            };
                // Iterate over each city to count the number of provinces.
            for (int i = 0; i < num_cities; ++i) {
                // If the city is not yet visited, it is part of a new province.
                if (!visited[i]) {
                    dfs(i); // Perform DFS to visit all cities in the current province.
                    ++province_count; // Increment the count of provinces.
                }
            }
        
            // Return the total number of provinces found.
            return province_count;
        }
};
