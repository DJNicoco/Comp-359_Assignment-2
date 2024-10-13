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

Graph prismGraph(int baseGraphSize){
  Graph prism;
    
    //Create base graph (path graph)
    for (int i = 0; i < baseGraphSize; ++i) {
        prism.addNode(); //Add nodes for the base
    }
    //Create upper graph by adding nodes
    for (int i = 0; i < baseGraphSize; ++i) {
        prism.addNode(); //Add nodes for the upper base
    }
    //Add edges for the base graph 
    for (int i = 0; i < baseGraphSize; ++i) {
        prism.addEdge(i, (i + 1) % baseGraphSize); // Connect base nodes in a cycle
    }
    //Add edges for the upper graph 
    for (int i = baseGraphSize; i < 2 * baseGraphSize; ++i) {
        prism.addEdge(i, ((i + 1) % baseGraphSize) + baseGraphSize); // Connect upper nodes in a cycle
    }
    //Add edges between the base and upper graph
    for (int i = 0; i < baseGraphSize; ++i) {
        prism.addEdge(i, i + baseGraphSize); // Connect base nodes to the corresponding upper nodes
    }
    return prism; // Return the resulting prism graph
}

int main() {
    int baseGraphSize = 6; // Size of the base graph for the prism

    //Create a prism graph based on the base graph size
    Graph prism = prismGraph(baseGraphSize);

    //Print the resulting prism graph
    prism.printGraph();

    return 0;
}