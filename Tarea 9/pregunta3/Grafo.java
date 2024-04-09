package pregunta3;

import java.util.HashSet;
import java.util.LinkedList;
import java.util.ListIterator;

public class Grafo {
    /**
     * Graph representation as Adjacencies Linked List
     */
    private LinkedList<LLNode> graph;
    /**
     * Nodes in the graph
     */
    private HashSet<Integer> nodes;
    /**
     * Edges in the graph
     */
    private HashSet<Edge> edges;

    /**
     * Gets all the nodes/vertices of the graph
     * 
     * @return Nodes/Vertices of the graph
     */
    public HashSet<Integer> Vertices() {
        return nodes;
    }

    /**
     * Gets all the nodes/vertices of the graph
     * 
     * @return Edges of the graph
     */
    public HashSet<Edge> Edges() {
        return edges;
    }

    /**
     * Gets a node object from the <code>graph<\code> that is associated to an
     * integer id. Returns nulls if the node isn't in the graph.
     * 
     * @param nodeID Node id to look for
     * @return Node associated to the node id
     */
    public LLNode GetNode(int nodeID) {
        if (!nodes.contains(nodeID))
            return null;
        else {
            ListIterator<LLNode> iterator = graph.listIterator();
            while (iterator.hasNext()) {
                LLNode act = iterator.next();
                if (act.getID() == nodeID)
                    return act;
            }
            return null;
        }
    }

    /**
     * Inserts a node in the graph with the choosen ID. If the node is already in
     * the graph, it does nothing.
     * 
     * @param nodeID Node ID of the node to add.
     */
    public void InsertNode(int nodeID) {
        if (nodes.contains(nodeID))
            return;
        else {
            LLNode lnode = new LLNode(nodeID);
            nodes.add(nodeID);
            graph.add(lnode);
        }
    }

    /**
     * Adds an edge between the node <code>from<\code> and the node <code>to<\code>.
     * The edge goes from both nodes (undirected graph).
     * 
     * @param edge Edge in pair representation.
     */
    public void AddEdge(Edge edge) {
        if (!nodes.contains(edge.from) || !nodes.contains(edge.to))
            return;
        else {
            this.GetNode(edge.from).setSucesor(edge.to);
            edges.add(edge);
        }
    }

    /**
     * Gets the adjancent nodes of a node from a graph. If the node with the
     * associated ID isn't in the graph, it returns null. If the node doesn't got
     * any adjacent nodes, it returns a empty linked list.
     * 
     * @param nodeID NodeID of the node to look for it adjacent nodes
     * @return Adjacent nodes of a node in the graph
     */
    public LinkedList<Integer> SucesorNodes(int nodeID) {
        if (!nodes.contains(nodeID)) {
            return null;
        } else {
            LLNode toGet = this.GetNode(nodeID);
            return toGet.getSucesors();
        }
    }

    public Grafo() {
        nodes = new HashSet<Integer>();
        graph = new LinkedList<LLNode>();
        edges = new HashSet<Edge>();
    }
}

class LLNode {
    private int id;
    private boolean isVisited = false;
    private LinkedList<Integer> suceNodes;

    public LLNode(int id) {
        this.id = id;
        this.suceNodes = new LinkedList<Integer>();
    }

    public int getID() {
        return id;
    }

    public LinkedList<Integer> getSucesors() {
        return suceNodes;
    }

    public void setSucesor(int suce) {
        suceNodes.add(suce);
    }

    public boolean isVisited() {
        return isVisited;
    }

    public void setVisited(boolean isVisited) {
        this.isVisited = isVisited;
    }

}

class Edge {

    // Edge attributes
    public int from;
    public int to;

    // Constructor to initialize pair
    public Edge(int from, int to) {
        // This keyword refers to current instance
        this.from = from;
        this.to = to;
    }
}
