from pyllist import sllist # type: ignore
import matplotlib.pyplot as plt

class Gridgraph:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.graph = {}
        

        for row in range(rows):
            for col in range(cols):
                node = (row,col)
                self.graph[node] = sllist()
                

                if row > 0:
                   self.add_edge(node,(row-1, col))
                if col > 0:
                  self.add_edge(node,(row, col-1))

    def add_edge(self, from_node, to_node):
        self.graph[from_node].append(to_node)
       
    def cartestian_product(self,graph1):
        product_graph = Gridgraph()

        for a in self.graph:
            for b in graph1.graph:
                product_graph.add_node((a,b))

        for a in self.garaph:
            for b in graph1.graph:
                for neighbor in self.graph[a]:
                    product_graph.add_edge((a,b),(neighbor,b))
                for neighbor in graph1.graph[b]:
                    product_graph.add_edge((a,b),(a,neighbor))
        return product_graph   
    
    def visualize(self):
        pos = {(row,col):(col,-row) for row,col in self.graph.keys()}
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

grid_graph=Gridgraph(5,9)
grid_graph.visualize()
