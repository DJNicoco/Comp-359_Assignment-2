import java.util.LinkedList;
import java.util.Arrays;

class Graph{

    //Sets the foundational framwork for building future graphs
    //This is an overarching adjacency list, to hold future linkedlists
    LinkedList<LinkedList<Integer>>Graph_Shell;
    int V;                           //# of nodes

    Graph(int NodesAmount){         //Constructor method creating new linkedlist to connect nodes with edges
        V = NodesAmount;
        Graph_Shell = new LinkedList<LinkedList<Integer>>();

        for (int i = 0; i < V; i++) {
            Graph_Shell.add(new LinkedList<Integer>());
        }
    }


    //This function defines an edge connecting two nodes
    void AddEdge(int v, int u){
        Graph_Shell.get(v).add(u);
        Graph_Shell.get(u).add(v);
    }


    //For respective graphs, prints non-empty nodes, displays connections between nodes made with edges
    void PrintGraph(int StartAt){
        for (int i = 0; i < V; i++) {
            if (!Graph_Shell.get(i).isEmpty()){
                System.out.println("Node " +(i+StartAt)+":" );
                for (int x: Graph_Shell.get(i))System.out.println(">Nodes connected: " +x);
                System.out.println(" ");

            }
        }
    }

    //Creates pairs of cartesian products
    static void Cartesian_Product(LinkedList<Integer>GRID, LinkedList<Integer>CROWN){
        int count =1;
        for (int i=0; i<GRID.size();i++){
            int Grid_Node = GRID.get(i);

            for (int j=0; j<CROWN.size();j++){
                int Crown_Node = CROWN.get(j);
                System.out.println("Cartesian Node #" + count+": " +"{" + Grid_Node +", " + Crown_Node+"} ");
                count++;

            }

        }
    } 
       
}

public class MT_2{

    public static void main (String[] args){

        //Grid graph, 3 by 3 nodes (9 nodes total), connected by 12 edges
        //Allocates a designated number of nodes to the graph using AddEdge from the Graph class
        //Connects nodes together with edges
        Graph grid = new Graph(8);  
        grid.AddEdge(0,1);
        grid.AddEdge(0,2);
        grid.AddEdge(1,3);
        grid.AddEdge(2,3);
        grid.AddEdge(2,4);
        grid.AddEdge(3,5);
        grid.AddEdge(4,5);
        grid.AddEdge(4,6);
        grid.AddEdge(5,7);
        grid.AddEdge(6,7);
        

        System.out.println("----------------------------------------------------------------------");
        System.out.println("Grid Graph:");
        System.out.println("----------------------------------------------------------------------");
        grid.PrintGraph(0);

        //Crown graph(complete bipartite graph w/0 horiz. edges), 2 by 3 nodes (6 nodes total), connected by 6 edges
        //Allocates a designated number of nodes to the graph using AddEdge from the Graph class
        //Connects nodes together with edges
        Graph crown = new Graph(14);  //Actual node count is 6
        crown.AddEdge(8,11);
        crown.AddEdge(8,13);
        crown.AddEdge(10,9);
        crown.AddEdge(10,13);
        crown.AddEdge(12,9);
        crown.AddEdge(12,11);

        System.out.println("----------------------------------------------------------------------");
        System.out.println("Crown Graph:");
        System.out.println("----------------------------------------------------------------------");
        crown.PrintGraph(-8);


        //Fills arrays for grid graph and crown graph respectively, preparing them for the cartesian product
        LinkedList<Integer>GridVerticeSet = new LinkedList<>();
        for(int i = 0; i<grid.V;i++){
            GridVerticeSet.add(i);
        }

        LinkedList<Integer>CrownVerticeSet = new LinkedList<>();
        for(int i = 0; i<6;i++){
            CrownVerticeSet.add(i+8);
        }


        System.out.println("----------------------------------------------------------------------");
        System.out.println("Cartesian Product:");
        System.out.println("----------------------------------------------------------------------");

        //Implements Cartesian Product
        Graph.Cartesian_Product(GridVerticeSet, CrownVerticeSet);

    }

}