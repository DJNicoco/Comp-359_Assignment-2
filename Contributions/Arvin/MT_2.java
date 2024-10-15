import java.util.LinkedList;

class Graph{
    LinkedList<LinkedList<Integer>>Graph_Shell;
    int V;                           //# of nodes

    Graph(int NodesAmount){         //Constructor
        V = NodesAmount;
        Graph_Shell = new LinkedList<LinkedList<Integer>>();

        for (int i = 0; i < V; i++) {
            Graph_Shell.add(new LinkedList<Integer>());
        }
    }


    void AddEdge(int v, int u){
        Graph_Shell.get(v).add(u);
        Graph_Shell.get(u).add(v);
    }


    void PrintGraph(){
        for (int i = 0; i < V; i++) {
            System.out.println("Node " +i+":" );
            for (int x: Graph_Shell.get(i))System.out.println(">Node # connected: " +x);
            System.out.println();
        }
    }
}

/*
class Node{

}
*/

public class MT_2{

    public static void main (String[] args){

        Graph grid = new Graph(9);   
        grid.AddEdge(0,3);
        grid.AddEdge(0,1);
        grid.AddEdge(1,2);
        grid.AddEdge(1,4);
        grid.AddEdge(2,5);
        grid.AddEdge(3,4);
        grid.AddEdge(3,6);
        grid.AddEdge(4,7);
        grid.AddEdge(5,8);
        grid.AddEdge(6,7);
        grid.AddEdge(7,8);
        grid.AddEdge(4,5);

        System.out.println("----------------------------------------------------------------------");
        System.out.println("Grid Graph:");
        System.out.println("----------------------------------------------------------------------");
        grid.PrintGraph();



        Graph crown = new Graph(6); 
        crown.AddEdge(0,4);
        crown.AddEdge(0,5);
        crown.AddEdge(1,3);
        crown.AddEdge(1,5);
        crown.AddEdge(2,3);
        crown.AddEdge(2,4);

        System.out.println("----------------------------------------------------------------------");
        System.out.println("Crown Graph:");
        System.out.println("----------------------------------------------------------------------");
        crown.PrintGraph();

    }

}