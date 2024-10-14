from pyllist import sllist
 #use the sllist data structure of pyllist library
 #Bookgraph to represent the structure of the graph
class Bookgraph:
    def __init__(self):
        self.graph = {}
#initializes an empty dictionary self.graph
    def add_node(self,node):
        self.graph[node] = sllist()
#Adds a new node to the graph and initializes an empty single-linked list for that node
    def add_edge(self, from_node, to_node):
        self.graph[from_node].append(to_node)
#store neighboring nodes of each node
    def cartesian_product(self, graph1):
        product_graph = Bookgraph()
#compute the Cartesian product of the current graph and another graph, and return a new graph
        for a in self.graph:
            for b in graph1.graph:
                product_graph.add_node((a,b))
#Use two for loops to travel all nodes of graph and create new modes
        for a in self.graph:
            for b in graph1.graph:
                for neighbor in self.graph[a]:
                    product_graph.add_edge((a,b),(neighbor,b))
                    # find the node adjacent to a and create an edge between it and (a, b)
                for neighbor in graph1.graph[b]:
                    product_graph.add_edge((a,b),(a,neighbor))
                    #Find the node adjacent to b and create an edge between it and (a, b)
        return product_graph
    
    def star_graph(self, m):
        for i in range (m+1):
            self.add_node(i)
        for i in range (1,m+1):
             self.add_edge(0,i)
#Define star graph, connect 0 and each node
    def path_graph(self):
        self.add_node(0)
        self.add_node(1)
        self.add_edge(0,1)
#Define path graph, connect 0 and 1

m=3
star_graph = Bookgraph()
star_graph.star_graph(m)
#Create a star graph with four nodes, node 0 connected to peripheral nodes 1,2,3
path_graph = Bookgraph()
path_graph.path_graph()
#Create a simple pathgraph
B_m = star_graph.cartesian_product(path_graph)
#Create the Cartesian product of a star graph and a path graph to get a book graph
print("Nodes in B_m are:")
print(B_m.graph.keys())
print("\nEdges in B_m:")
for node in B_m.graph:
    for neighbor in B_m.graph[node]:
        print(f"{node} -> {neighbor}")
#Print all nodes of B_m, as well as edges

