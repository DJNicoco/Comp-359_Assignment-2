#include <iostream>
#include <list>
#include <vector>
#include <iomanip>

class Graph {
public: 
    //Adjacency list representation using linked lists
    std::vector<std::list<int>> adjList;

    //Method to add a node to the graph
    void addNode(){
        adjList.emplace_back(); //Adds a new empty adjacency list for the new node
    }
    //Method to add an edge between two nodes
    void addEdge(int fromNode, int toNode){
        adjList[fromNode].push_back(toNode); //Add the edge from 'fromNode' to 'toNode'
        adjList[toNode].push_back(fromNode); //Add the edge from 'toNode' to 'fromNode'
    }

    //Method to print the graph's list
    void printGraph() const {
        std::cout << "Graph List Representation:\n";
        for (int i = 0; i < adjList.size(); i++){
            std::cout << "-> " << std::setw(2) << i << ": ";
            for (const auto &neighbour : adjList[i]){
                std::cout << "-> " << std::setw(2) << neighbour << " ";
            }
            std::cout << std::endl;
        }
    }
};

//Function to create path graph with n nodes
Graph pathGraph(int n){
    Graph path;
    for (int i = 0; i < n; i++){
        path.addNode(); //Adds nodes to the path graph
    }
    for (int i = 0; i < n - 1; i++){
        path.addEdge(i, i + 1); //Connects the nodes
    }
    return path;
}

//Function to create the cartesian product of two graphs
Graph cartesianProduct(const Graph &graph1, const Graph &graph2){
    Graph productGraph;

    int rows1 = graph1.adjList.size(); //number of nodes in the first graph
    int rows2 = graph2.adjList.size(); //number of nodes in the second graph

    //This creates nodes for the product
    for (int i = 0; i < rows1; i++){
        for (int j = 0; j < rows2; j++){
            productGraph.addNode();
        }
    }
    //This adds edges for the product
    for (int i = 0; i < rows1; i++){
        for (int j = 0; j < rows2; j++) {
            int currentNode = i * rows2 + j;

            //Connects to right neighbor in the same row
            if (j < rows2 - 1){
                int rightNeighbor = i * rows2 + (j + 1);
                productGraph.addEdge(currentNode, rightNeighbor);
            }
            //Connects to the neighbor below in the same column
            if (i < rows1 - 1){
                int bottomNeighbor = (i + 1) * rows2 + j;
                productGraph.addEdge(currentNode, bottomNeighbor);
            } 
            //This then connects to neighbors from the second graph
            for(const auto &neighbor : graph2.adjList[j]){
                productGraph.addEdge(currentNode, i * rows2 + neighbor);
            }
        }
    }
    return productGraph; //Returns the product graph
}

int main() {
    int m = 6; //number of nodes in path graph P_m
    int n = 3; //number of nodes in path graph P_n

    //This creates the path graphs
    Graph P_m = pathGraph(m);
    Graph P_n = pathGraph(n);

    //This creates the cartesian product to get the grid graph
    Graph gridGraph = cartesianProduct(P_m, P_n);

    //This prints the grid graph
    gridGraph.printGraph();
    
    return 0;
}
