package pregunta2;

/**
 * Class that applies DFS
 */
public class DFS {
    /**
     * Graph in which is going to be used DFS
     */
    private Grafo grafo;

    /**
     * Construct DFS
     * 
     * @param grafo Graph to apply DFS.
     */
    public DFS(Grafo grafo) {
        this.grafo = grafo;
    }

    /**
     * Start to run DFS recursively since node with u as identifier.
     * Taking into the account the matching
     * 
     * @param u source node.
     */
    public boolean DFSVisited(int u) {
        grafo.GetNode(u).setVisited(true);

        for (int v : grafo.SucesorNodes(u)) {

            LLNode node = grafo.GetNode(v);
            if (!node.isVisited()) {

                if (node.getMatch() < 0 || DFSVisited(v)) {
                    node.setMatch(u);
                    return true;
                }

            }
        }
        return false;
    }

}