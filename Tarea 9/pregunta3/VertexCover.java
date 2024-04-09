package pregunta3;

import java.io.IOException;
import java.lang.IllegalArgumentException;
import java.util.Set;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Iterator;

/**
 * Class that applies DFS
 */
public class VertexCover {
    /**
     * Loads edges based on isPrime relationship.
     * 
     * @param E     set of edges
     * @param grafo Graph where the edge is added. It is modified directly.
     */
    static void loadEdges(LinkedList<Edge> E, Grafo grafo) {

        for (Edge e : E) {
            grafo.AddEdge(e);
        }

    }

    /**
     * Loads a graph from a set of integers.
     * 
     * @param V Set of vertex
     * @return Graph representation
     * 
     */
    static Grafo loadGraph(Set<Integer> V) throws IOException {
        Grafo result = new Grafo();

        for (Integer number : V) {
            result.InsertNode(number);
        }

        return result;
    }

    static HashSet<Integer> approximateVertexCover(Grafo grafo) {
        HashSet<Integer> VC = new HashSet<Integer>();
        HashSet<Edge> E = grafo.Edges();

        Iterator<Edge> iterator = E.iterator();
        while (iterator.hasNext()) {
            Edge edge = iterator.next();
            if (!(VC.contains(edge.from) || VC.contains(edge.to))) {
                VC.add(edge.from);
                VC.add(edge.to);
            }
        }

        return VC;
    }


    public static void main(String[] args) throws IOException, IllegalArgumentException {
        Set<Integer> V = new HashSet<Integer>();
        for (int i = 0; i < 7; i++) {
            V.add(i);
        }

        Grafo g = loadGraph(V);

        LinkedList<Edge> E = new LinkedList<>();
        E.add(new Edge(0, 1));
        E.add(new Edge(0, 2));
        E.add(new Edge(2, 3));
        E.add(new Edge(3, 4));
        E.add(new Edge(4, 5));
        E.add(new Edge(4, 6));
        E.add(new Edge(5, 6));
        loadEdges(E, g);

        HashSet<Integer> VC = approximateVertexCover(g);
        System.out.println("GRAFO 1");
        for (int v : VC) {
            System.out.println(v);
        }

        Set<Integer> V2 = new HashSet<Integer>();
        for (int i = 0; i < 6; i++) {
            V2.add(i);
        }

        Grafo g2 = loadGraph(V2);

        LinkedList<Edge> E2 = new LinkedList<>();
        E2.add(new Edge(0, 3));
        E2.add(new Edge(0, 4));
        E2.add(new Edge(0, 5));
        E2.add(new Edge(1, 5));
        E2.add(new Edge(2, 5));
        loadEdges(E2, g2);

        HashSet<Integer> VC2 = approximateVertexCover(g2);
        System.out.println("GRAFO 2");
        for (int v : VC2) {
            System.out.println(v);
        }
    }
}