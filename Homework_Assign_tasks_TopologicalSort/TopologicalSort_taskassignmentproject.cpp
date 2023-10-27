#include <iostream>
#include <vector>
#include <list>
#include <stack>

class Digraph {
public:
    Digraph(int V);  // Constructor
    ~Digraph();      // Destructor

    void addEdge(int v, int w);  // Add a directed edge from v to w

    bool isDAG();  // Check if the graph is a Directed Acyclic Graph (DAG)  

    void topologicalSort();  // Perform topological sort

private:
    int V;                 // Number of vertices
    std::list<int>* adj;   // Adjacency list
    bool isDAGUtil(int v, bool visited[], bool stack[]);

    struct Node {
        int data;
        Node* next;
    };

    Node* createNode(int data) {
        Node* newNode = new Node();
        newNode->data = data;
        newNode->next = nullptr;
        return newNode;
    }

    Node* insertFront(Node* head, int data) {
        Node* newNode = createNode(data);
        newNode->next = head;
        head = newNode;
        return head;
    }

    void deleteList(Node* head) {
        while (head) {
            Node* temp = head;
            head = head->next;
            delete temp;
        }
    }
};

Digraph::Digraph(int V) {
    this->V = V;
    adj = new std::list<int>[V];
}

Digraph::~Digraph() {
    delete[] adj;
}

void Digraph::addEdge(int v, int w) {
    adj[v].push_back(w);
}

bool Digraph::isDAGUtil(int v, bool visited[], bool stack[]) {
    if (!visited[v]) {
        visited[v] = true;
        stack[v] = true;

        for (const auto& neighbor : adj[v]) {
            if (!visited[neighbor] && isDAGUtil(neighbor, visited, stack)) {
                return true;
            }
            else if (stack[neighbor]) {
                return true;
            }
        }
    }
    stack[v] = false;
    return false;
}

bool Digraph::isDAG() {
    bool* visited = new bool[V];
    bool* stack = new bool[V];

    for (int i = 0; i < V; i++) {
        visited[i] = false;
        stack[i] = false;
    }

    for (int i = 0; i < V; i++) {
        if (isDAGUtil(i, visited, stack)) {
            delete[] visited;
            delete[] stack;
            return false;
        }
    }

    delete[] visited;
    delete[] stack;
    return true;
}

void Digraph::topologicalSort() {
    if (!isDAG()) {
        std::cout << "The graph is not a Directed Acyclic Graph (DAG)." << std::endl;
        return;
    }

    std::stack<int> stack;
    bool* visited = new bool[V];
    for (int i = 0; i < V; i++) {
        visited[i] = false;
    }

    for (int i = 0; i < V; i++) {
        if (!visited[i]) {
            std::stack<int> nodeStack;
            nodeStack.push(i);

            while (!nodeStack.empty()) {
                int v = nodeStack.top();
                nodeStack.pop();

                if (!visited[v]) {
                    visited[v] = true;

                    for (const auto& neighbor : adj[v]) {
                        if (!visited[neighbor]) {
                            nodeStack.push(neighbor);
                        }
                    }

                    stack.push(v);
                }
            }
        }
    }

    // Print the topological order
    std::cout << "Topological Order:" << std::endl;
    while (!stack.empty()) {
        std::cout << stack.top() << " ";
        stack.pop();
    }
    std::cout << std::endl;

    delete[] visited;
}

int main() {
    int V;  // Number of vertices
    std::vector<std::string> tasks;

    // Prompt the user to enter the number of tasks and their descriptions
    std::cout << "Enter the number of tasks: ";
    std::cin >> V;
    std::cin.ignore();  // Consume newline character
    for (int i = 0; i < V; i++) {
        std::cout << "Enter the description for Task " << i << ": ";
        std::string task;
        std::getline(std::cin, task);
        tasks.push_back(task);
    }

    Digraph graph(V);

    // Prompt the user to specify the order relations
    std::cout << "Specify order relations (e.g., '3 1' means Task 3 must precede Task 1):" << std::endl;
    int task1, task2;
    while (true) {
        std::cout << "Enter order relation (or -1 -1 to stop): ";
        std::cin >> task1 >> task2;
        if (task1 == -1 || task2 == -1) {
            break;
        }
        if (task1 < 0 || task1 >= V || task2 < 0 || task2 >= V) {
            std::cout << "Invalid task numbers. Please try again." << std::endl;
        }
        else {
            graph.addEdge(task1, task2);
        }
    }

    if (graph.isDAG()) {
        std::cout << "The graph is a Directed Acyclic Graph (DAG)." << std::endl;
    }
    else {
        std::cout << "The graph is not a Directed Acyclic Graph (DAG)." << std::endl;
    }

    graph.topologicalSort();

    return 0;
}
