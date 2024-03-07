from math import ceil, log2

class Node:
    def __init__(self, key):
        """ Inicializar nodo que guarda para el arbol segmentado
        """
        self.key = key
        self.parent = None
        self.depth = 0
        self.size = 0
        self.head = None
        self.pos = None
        self.heavy = None
        self.flag = False

    def __eq__(self, other):
        return (other is not None and self.key == other.key)

    def __hash__(self):
        return hash(str(self.key))

    def __repr__(self):
        return "NODE (key: %s, parent: %s, heavy: %s, depth: %s, size: %s, pos: %s, head: %s)" % (
            self.key,
            self.parent.key if self.parent is not None else -1,
            self.heavy.key if self.heavy is not None else -1,
            self.depth,
            self.size,
            self.pos,
            self.head,
        )
        
class SegmentTreeNode:
    def __init__(self, data=False):
        """ Inicializar nodo que guarda para el arbol segmentado
        """
        self.data = data
        self.right = None
        self.left = None
        
    def __repr__(self):
        return "NODE (data: %s)" % (
            self.data,
        )


class Tree:

    def __init__(self):
        self.tree = {}
        self.n = 0

    # Function to add an edge to graph

    def add_node(self, u):
        self.tree[u] = []
        self.n += 1

    def add_edge(self, u, v, flag):
        if self.tree.get(u) is None:
            self.tree[u] = []
        v.flag = flag
        self.tree[u].append(v)

    def get_root(self):
        for nd in self.tree.keys():
            if (nd.parent is None):
                return nd

    # A function used by DFS

    def dfs(self, v):

        size = 1
        max_path_size = 0

        for neighbour in self.tree[v]:
            if neighbour != v.parent:
                neighbour.parent = v
                neighbour.depth = v.depth + 1
                path_size = self.dfs(neighbour)
                size += path_size

                if path_size > max_path_size:
                    max_path_size = path_size
                    v.heavy = neighbour

        v.size = size
        return size

    def decompose_helper(self, v, h, current_pos, barray):
        v.head = h.key
        v.pos = current_pos[0]
        barray[current_pos[0]] = SegmentTreeNode(v.flag)
        current_pos[0] += 1

        if v.heavy is not None:
            self.decompose_helper(v.heavy, h, current_pos, barray)

        for neighbour in self.tree[v]:
            if neighbour != v.parent and neighbour != v.heavy:
                self.decompose_helper(neighbour, neighbour, current_pos, barray)
                
    def decompose(self, v, h):
        current_pos = [0]
        barray = [None for _ in range(self.n)]
        self.decompose_helper(v, h, current_pos, barray)
        return barray
        

class SegmentTree:
    def __init__(self, barray, get_parent_from_children=lambda x, y:(x and y), stop_function=lambda x: x):
        self.barray = barray

        n = len(barray)
        n_levels = ceil(log2(n) + 1)
        max_len = 2**n_levels - 1

        self.from_array_size = n
        self.tree = [SegmentTreeNode() for _ in range(max_len)]
        self.get_parent_from_children = get_parent_from_children
        self.stop_function = stop_function

        # Construimos el arbol al inicializarlo
        self.create_tree(0, 0, n - 1, barray)

    def create_tree(self, current, lower, upper, t):
        """ Se construye el arbol de parentesis
        """

        # Condicion de parada de la recursion
        if upper == lower:
            self.tree[current] = self.stop_function(self.barray[lower])
            return self.tree[current]

        # Segmentamos a la mitad
        mid = (lower + upper) // 2

        # Obtenemos el padre a partir de los hijos hasta llegar a la raiz
        self.tree[current] = self.get_parent_from_children(
            self.create_tree(2 * current + 1, lower, mid, t),
            self.create_tree(2 * current + 2, mid + 1, upper, t),
        )

        return self.tree[current]
    
    def query_tree_helper(self, current, lower_range, upper_range, lower, upper):
        if lower_range>=lower and upper_range<=upper:
            return self.tree[current]
        if lower_range>upper or upper_range<lower:
            return SegmentTreeNode()
        
        # Segmentamos a la mitad
        mid = (lower_range + upper_range) // 2
        
        # Obtenemos el padre a partir de los hijos hasta llegar a la raiz
        self.tree[current] = self.get_parent_from_children(
            self.query_tree_helper(2 * current + 1, lower_range, mid, lower, upper),
            self.query_tree_helper(2 * current + 2, mid + 1, upper_range, lower, upper),
        )

        return self.tree[current]
    
    def query_tree(self, lower, upper):
        
        return self.query_tree_helper(0,  0, self.from_array_size - 1, lower, upper)
        

def for_all(left, right):
    parent = SegmentTreeNode()
    parent.data = left.data and right.data
    parent.left = left
    parent.right = right
    return parent

def exist(left, right):
    parent = SegmentTreeNode()
    parent.data = left.data or right.data
    parent.left = left
    parent.right = right
    return parent


def main():
    tree = Tree()

    n = 11
    for i in range(n):
        tree.add_node(Node(i))

    nodes = list(tree.tree.keys())
    tree.add_edge(nodes[0], nodes[1], True)
    tree.add_edge(nodes[0], nodes[2], True)
    tree.add_edge(nodes[0], nodes[3], False)
    tree.add_edge(nodes[1], nodes[4], False)
    tree.add_edge(nodes[1], nodes[5], True)
    tree.add_edge(nodes[2], nodes[6], True)
    tree.add_edge(nodes[5], nodes[7], False)
    tree.add_edge(nodes[6], nodes[8], True)
    tree.add_edge(nodes[7], nodes[9], False)
    tree.add_edge(nodes[7], nodes[10], True)

    root = tree.get_root()
    
    tree.dfs(root)

    barray = tree.decompose(root, root)

    segment_tree = SegmentTree(barray, for_all)
    print("----FOR ALL----")
    print(segment_tree.query_tree(0, 1).data)
    print(segment_tree.query_tree(6, 9).data)
    print(segment_tree.query_tree(0, 10).data)

    print("\n----EXIST----")
    segment_tree = SegmentTree(barray, exist)
    print(segment_tree.query_tree(3, 4).data)
    print(segment_tree.query_tree(0, 4).data)
    print(segment_tree.query_tree(0, 10).data)

if __name__ == "__main__":
    main()
