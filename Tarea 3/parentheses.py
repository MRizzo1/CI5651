from math import ceil, log2


class Node:
    def __init__(self):
        self.n_balanced = 0
        self.open = 0
        self.closed = 0

    def __repr__(self):
        return "NODE (n_balanced: %s, open: %s, closed: %s)" % (
            self.n_balanced,
            self.open,
            self.closed,
        )


class ParenthesesSegmentTree:
    def __init__(self, text):
        self.text = text

        n = len(text)
        n_levels = ceil(log2(n) + 1)
        max_len = 2**n_levels - 1

        self.text_size = n
        self.tree = [Node() for _ in range(max_len)]
        self.create_tree(0, 0, n - 1, text)

    def get_parent_from_children(self, left, right):
        parent = Node()
        minBalanced = min(left.open, right.closed)
        parent.n_balanced = left.n_balanced + right.n_balanced + minBalanced
        parent.open = left.open + right.open - minBalanced
        parent.closed = left.closed + right.closed - minBalanced
        return parent

    def create_tree(self, current, lower, upper, t):
        if upper == lower:
            self.tree[current].n_balanced = 0
            
            if (t[lower] == "("): 
                self.tree[current].open = 1
            else:
                self.tree[current].closed = 1
            
            return self.tree[current]

        mid = (lower + upper) // 2

        self.tree[current] = self.get_parent_from_children(
            self.create_tree(2 * current + 1, lower, mid, t),
            self.create_tree(2 * current + 2, mid + 1, upper, t),
        )

        return self.tree[current]

    def query(self, current, total_lower, total_upper, lower, upper):
        if total_lower >= lower and total_upper <= upper:
            return self.tree[current]
        if total_lower > upper or total_upper < lower:
            return Node()

        mid = (total_lower + total_upper) // 2

        return self.get_parent_from_children(
            self.query(2 * current + 1, total_lower, mid, lower, upper),
            self.query(2 * current + 2, mid + 1, total_upper, lower, upper),
        )
        
    def max_bp(self, lower, upper):
        return 2 * self.query(0, 0, self.text_size - 1, lower, upper).n_balanced
        

if __name__ == '__main__':
    text = "())(())(())("
    print("TEXT: ", text)
    sm = ParenthesesSegmentTree(text)
    lower = 3
    upper = 10
    result = sm.max_bp( lower, upper)
    print("For %s and %s: " % (lower, upper), sm.max_bp( lower, upper))
    
    lower = 0
    upper = len(text)-1
    result = sm.max_bp( lower, upper)
    print("For %s and %s: " % (lower, upper), sm.max_bp( lower, upper))
    
    text = ")(())(()"
    print("\nTEXT: ", text)
    sm = ParenthesesSegmentTree(text)
    lower = 3
    upper = 5
    result = sm.max_bp( lower, upper)
    print("For %s and %s: " % (lower, upper), sm.max_bp( lower, upper))
    
    lower = 0
    upper = len(text)-1
    result = sm.max_bp( lower, upper)
    print("For %s and %s: " % (lower, upper), sm.max_bp( lower, upper))


