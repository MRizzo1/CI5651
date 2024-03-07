from math import ceil, log2


class SegmentTreeNode:
    def __init__(self, data=0):
        """ Inicializar nodo que guarda para el arbol segmentado
        """
        self.data = data
        self.right = None
        self.left = None

    def __repr__(self):
        return "NODE (data: %s left: %s, right: %s)" % (
            self.data,
            self.left.data if self.left is not None else -1,
            self.right.data if self.right is not None else -1
        )

def build_tree(current, lower_range, upper_range, base_array):
    if lower_range + 1 == upper_range:
        current.data = 0
        return
    
    # Segmentamos a la mitad
    mid = (lower_range + upper_range) // 2
    
    current.left = SegmentTreeNode()
    current.right = SegmentTreeNode()
    
    build_tree(current.left, lower_range, mid, base_array)
    build_tree(current.right, mid, upper_range, base_array)
    
    current.data = current.left.data + current.right.data

def query_tree(prev, current, lower_range, upper_range, k):
    if lower_range + 1 == upper_range:
        return lower_range

    # Segmentamos a la mitad
    mid = (lower_range + upper_range) // 2
    data = prev.left.data - current.left.data

    if data >= k:
        return query_tree(prev.left, current.left, lower_range, mid, k)
    
    return query_tree(prev.right, current.right, mid, upper_range, k - data)


def update_tree(current, lower_range, upper_range, pos):   
     
    if pos < lower_range or pos > upper_range or lower_range > upper_range:
        return current

    if lower_range + 1 == upper_range:
        return SegmentTreeNode(current.data + 1)

    # Segmentamos a la mitad
    mid = (lower_range + upper_range) // 2
    
    parent = SegmentTreeNode(current.data + 1)
    parent.left = update_tree(current.left, lower_range, mid, pos)
    parent.right = update_tree(current.right, mid, upper_range, pos)
    
    return parent


def main():
    
    n, q = map(int, input().split())

    barray = [0 for _ in range(n)]
    
    for i in range(n):
        barray[i] = int(input())
    
    barray = sorted(barray)
    n = len(barray)

    count = 0
    mapIndex = {}
    mapOcur = {}
    
    r = SegmentTreeNode()
    build_tree(r, 0, n, barray)
    
    tree = [r] + [None for _ in range(n - 1)]
        
    for e in barray:
        mapIndex[e] = count
        mapOcur[count] = e
        count += 1

    for i in range(n):
        tree[i] = update_tree(tree[i] if i == 0 else tree[i - 1], 0, count, mapIndex[barray[i]])

    
    for _ in range(q):
        l, r, k = map(int, input().split())
        l -=1
        r -=1
        print("RESPUESTA QUE NO ME DA BIEN", mapOcur.get(query_tree(tree[r], tree[l] if l == 0 else tree[l - 1], 0, count, k), None))


if __name__ == "__main__":
    main()
