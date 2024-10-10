from pyllist import sllist # type: ignore
import matplotlib.pyplot as plt

class Gridgraph:
    def __init__(self):
        self.graph = {}
    
    def add_node(self, node):
        self.graph[node] = sllist()
                
    def add_edge(self, from_node, to_node):
        self.graph[from_node].append(to_node)
       
    def cartestian_product(self,graph1):
        product_graph = Gridgraph()

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

def path_graph(n):
    path = Gridgraph()
    for i in range(n):
        path.add_node(i)
        if i >0:
            path.add_edge(i,i-1)
            path.add_edge(i-1,i)
    return path 
    
def visualize(self):
    pos = {node:(node[1],-node[0]) for node in self.graph.keys()}
    plt.figure(figsize=(10,10))

    for node in self.graph:
        for nearnode in self.graph[node]:
            x = [pos[node][0],pos[nearnode][0]]
            y = [pos[node][1],pos[nearnode][1]]
            plt.plot(x,y,color='blue', linewidth=1 )

    for node in self.graph:
        plt.scatter(pos[node][0],pos[node][1],color='lightgreen')
        plt.text(pos[node][0],pos[node][1],str(node),fontsize=10,ha='center',va='center')

    plt.title("Grid Graph Visualization")
    plt.axis('off')
    plt.show()

m = 5
n = 4
P_m = path_graph(m)
P_n = path_graph(n)
grid_graph = P_m.cartestian_product(P_n)
visualize(grid_graph)