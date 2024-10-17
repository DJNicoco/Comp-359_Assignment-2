# Comp 359 Assignment 2

Link to Github Repo: https://github.com/DJNicoco/Comp-359_Assignment-2.git

Our topic

11. implement a "multiplication" operation between two input graphs
  * implement your own graph data structure
    * add nodes
    * connect nodes
  * implement connections with linked-lists (use a library API for the lists)
  * Wolfram Mathworld: Graph Cartesian Product
    * https://mathworld.wolfram.com/GraphCartesianProduct.html
    * focus on the statement cited as from Harary, 1994, and this is easiest to create a new graph with the vertices described and edges between them
   
## Contributions:

Nicole - Wrote the C++ code using a grid graph/prism graph and README <br>
Teny - Wrote the Python code using a grid graph/book graph <br>
Arvin - Wrote the Java code using a grid graph/crown graph <br>

## Introduction into Graph Cartesian Product

The Cartesian product of two graphs 𝐺 and H creates a new graph where each vertex in the product graph represents a pair of nodes: one from graph G and one from graph H.<br>
The edges in the product graph are determined when the edges come from graph G, where the nodes from graph H stay the same and the nodes from graph G change. And when the edges come from graph H, the nodes from graph G stay the same and the nodes from graph H change. <br>
The product graph preserves the structure of both graphs, G and H, but in different parts of the graph. <br>

## Analysis Framework

In this assignment, we each focused on implementing the Graph Cartesian Product in different programming languages: C++, Python, and Java.  We all started with the same first graph, the grid graph, while each of us selected a different second graph to showcase how the Cartesian Product function would work with the different graphs in different languages. <br>

Teny implemented two types of graph structures in Python using the Graph Cartesian Product. First, he created a Gridgraph class to represent the grid graph, where each node is connected to its neighboring nodes. The Cartesian Product function combined two path graphs to form this grid graph, and the results were visualized using the Matplotlib library. Teny also developed a Bookgraph class, starting with a star graph that has a central node connected to other nodes, as well as a simple path graph composed of two points, 0 and 1. Then, the Bookgraph is created by taking the Cartesian product of the star graph and the simple path graph.

Arvin implemented two types of graphs in Java using the Graph Cartesian Product. First, he created a Graph class, which sets the framework for building future graphs, and developed methods for creating a new linked list to connect the nodes with edges. Arvin created the grid graph using 3 by 3 nodes connected by 12 edges and developed the crown graph, which consists of 2 by 3 nodes connected by 6 edges. To prepare for the Cartesian Product, he filled Linkedlists for the two graphs and then implemented the Cartesian Product function. The Cartesian product is being carried out between the grid graph and the crown graph.

## Results

For my part, I focused on implementing the C++ code. In my implementation, I created two types of graphs: the grid graph and the prism graph. The grid graph was the most common structure with our implementations and I picked a unique second graph called a prism graph. <br>
To create these graphs, I developed three methods: one for adding a node to the graph, one for adding an edge between two nodes, and one for printing the graph's list of nodes and edges. <br>

Additionally, I implemented two functions: one to create a path graph with n nodes, and another that computes the Cartesian product of two graphs. For the prism graph, I developed a function that creates the prism graph based on an input base graph, combining two parallel paths and connecting their corresponding nodes to form the prism.

Below is the grid graph output: <br>
![image](https://github.com/user-attachments/assets/be35dffd-1425-434d-9476-f7b7d86323b7) <br>

Below is the prism graph output: <br>
![image](https://github.com/user-attachments/assets/f56882c0-7db0-49ff-9668-d8b3c970f9ca)

## References

Agarwal, K. (2020, May 11). How to implement a graph in Java using ArrayList [Video]. YouTube. https://www.youtube.com/watch?v=UhFfdBdHCJM <br>
GeeksforGeeks. (2024, July 29). Cartesian product of two sets. GeeksforGeeks. Retrieved October 14, 2024, from https://www.geeksforgeeks.org/cartesian-product-two-sets/ <br>
GeeksforGeeks. (2024, July 1). C++ program to implement adjacency list. GeeksforGeeks. Retrieved October 14, 2024, from https://www.geeksforgeeks.org/cpp-program-to-implement-adjacency-list/ <br>
GeeksforGeeks. (2023, April 12). Java program to represent graphs using linked list. GeeksforGeeks. Retrieved October 14, 2024, from https://www.geeksforgeeks.org/java-program-to-represent-graphs-using-linked-list/ <br>
Sine, V. (2020, September 22). What is the Cartesian Product of Graphs? (Discrete Math) +3 examples! [Video]. YouTube. https://www.youtube.com/watch?v=c6LR9B2idQk <br>
Weisstein, E. W. (n.d.). Graph Cartesian product. Wolfram MathWorld. Retrieved October 14, 2024, from https://mathworld.wolfram.com/GraphCartesianProduct.html <br>




