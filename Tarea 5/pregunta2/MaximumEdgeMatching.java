package pregunta2;

import java.io.IOException;
import java.lang.IllegalArgumentException;
import java.util.Set;
import java.util.HashSet;
import java.util.Iterator;

public class MaximumEdgeMatching {
	static boolean isPrime(int num) {
		if (num <= 1) {
			return false;
		}
		for (int i = 2; i * i <= num; i++) {
			if (num % i == 0) {
				return false;
			}
		}
		return true;
	}

	/**
	 * Loads edges based on isPrime relationship.
	 * 
	 * @param C     set of vertex
	 * @param grafo Graph where the edge is added. It is modified directly.
	 */
	static void loadEdges(Set<Integer> C, Grafo grafo) {

		Iterator<Integer> iter1 = C.iterator();

		while (iter1.hasNext()) {
			int x = iter1.next();
			Iterator<Integer> iter2 = C.iterator();
			while (iter2.hasNext()) {
				int y = iter2.next();
				if (x != y) {
					int sum = x + y;
					if (isPrime(sum)) {
						grafo.AddEdge(x, y);

					}
				}
			}
		}

	}

	/**
	 * Loads a graph from a set of integers.
	 * 
	 * @param C Set of vertex
	 * @return Graph representation
	 * 
	 */
	static Grafo loadGraph(Set<Integer> C) throws IOException {
		Grafo result = new Grafo();

		for (Integer number : C) {
			result.InsertNode(number);
		}

		loadEdges(C, result);

		return result;
	}

	/**
	 * We need the minimum number of removals in C to have no pairs of number
	 * wich sum results in a prime number (this being the relation to set an edge
	 * between the nodes).
	 * So we want to remove all the edges in the graph by removing smallest number
	 * of vertices; i.e., we want the minimum vertex cover.
	 * By Konig theorem, the number of vertices in minimum vertex cover is elistual
	 * to the number of edges in maximum matching in bipartite graphs.
	 * 
	 * @param g A bipartite graph :D
	 * @return max
	 * 
	 */
	static int maximumEdgeMatching(Grafo g) {

		DFS dfs = new DFS(g);

		int result = 0;

		for (int u : g.Vertices()) {
			if (dfs.DFSVisited(u))
				result++;
		}
		return result;
	}

	public static void main(String[] args) throws IOException, IllegalArgumentException {
		Set<Integer> C = new HashSet<Integer>();
		C.add(1);
		C.add(2);
		C.add(3);

		Grafo g = loadGraph(C);

		System.out.println(maximumEdgeMatching(g));

		Set<Integer> C2 = new HashSet<Integer>();
		C2.add(1);
		C2.add(5);
		C2.add(8);

		Grafo g2 = loadGraph(C2);

		System.out.println(maximumEdgeMatching(g2));
	}

}
