from pyllist import sllist

class Bookgraph:
    def __init__(self):
        self.graph = {}

    def add_node(self,node):
        self.graph[node] = sllist()

    def add_edge(self, from_node, to_node):
        self.graph[from_node].append(to_node)

    def cartesian_product(self, graph1):
        product_graph = Bookgraph()

        for a in self.graph:
            for b in graph1.graph:
                product_graph.add_node((a,b))

        for a in self.graph:
            for b in graph1.graph:
                for neighbor in self.graph[a]:
                    product_graph.add_edge((a,b),(neighbor,b))
                for neighbor in graph1.graph[b]:
                    product_graph.add_edge((a,b),(a,neighbor))
        return product_graph
    
    def star_graph(self, m):
        for i in range (m+1):
            self.add_node(i)
        for i in range (1,m+1):
             self.add_edge(0,i)

    def path_graph(self):
        self.add_node(0)
        self.add_node(1)
        self.add_edge(0,1)

m=3
star_graph = Bookgraph()
star_graph.star_graph(m)

path_graph = Bookgraph()
path_graph.path_graph()

B_m = star_graph.cartesian_product(path_graph)

print("Nodes in B_m are:")
print(B_m.graph.keys())
print("\nEdges in B_m:")
for node in B_m.graph:
    for neighbor in B_m.graph[node]:
        print(f"{node} -> {neighbor}")
