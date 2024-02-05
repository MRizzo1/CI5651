from math import ceil, log2

# 
class Node:
    def __init__(self):
        """ Inicializar nodo que guarda para el arbol segmentado los siguientes datos
        n_balanced: numero de parentesis balanceados
        open: numero de parentesis que abres
        closed: numero de paretensis que cierran
        """
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
        """ Inicializar arbol segmentado de parentesis con
        text: texto con los parentesis a partir del cual se quiere generar el arbol
        text_size: longitud del texto indicado
        tree: estructura que almacena los nodos del arbol
        """
        self.text = text

        n = len(text)
        n_levels = ceil(log2(n) + 1)
        max_len = 2**n_levels - 1

        self.text_size = n
        self.tree = [Node() for _ in range(max_len)]
        
        # Construimos el arbol al inicializarlo
        self.create_tree(0, 0, n - 1, text)

    def get_parent_from_children(self, left, right):
        """ Se hace merge de los hijos para obtener el padre al regresar en la recursion
        """
        parent = Node()
        
        # Tomamos el minimo entre los nodos abiertos del hijo izquierdo y los cerrados del derecho
        # Esto nos da el minimo de parentesis balanceados entre los hijos por como se construye el arbol, es decir,
        # si left.open = 1 y right.closed = 4 entonces eso significa que al menos hay un parentesis que cierra el abierto y tenemos un match a ese punto.
        minBalanced = min(left.open, right.closed)
        
        # Sumamos el resultado del minimo a los balanceados
        parent.n_balanced = left.n_balanced + right.n_balanced + minBalanced
        
        # Restamos el minimo tanto del total de nodos abiertos como del total de los nodos cerrados entre ambos hijos
        # Esto con el fin de dejar indicados solo aquellos que no estan balanceados
        parent.open = left.open + right.open - minBalanced
        parent.closed = left.closed + right.closed - minBalanced
        return parent

    def create_tree(self, current, lower, upper, t):
        """ Se construye el arbol de parentesis
        """
        
        # Condicion de parada de la recursion
        if upper == lower:
            
            # Si ambos limites son iguales, significa que ya llegamos tan lejos como podiamos en ese camino del arbol, 
            # por ende, nos queda un solo caracter que revisar. No tenemos balanceados y es o parentesis cerrado o parentesis abierto
            self.tree[current].n_balanced = 0
            
            if (t[lower] == "("): 
                self.tree[current].open = 1
            else:
                self.tree[current].closed = 1
            
            return self.tree[current]

        # Segmentamos a la mitad
        mid = (lower + upper) // 2

        # Obtenemos el padre a partir de los hijos hasta llegar a la raiz
        self.tree[current] = self.get_parent_from_children(
            self.create_tree(2 * current + 1, lower, mid, t),
            self.create_tree(2 * current + 2, mid + 1, upper, t),
        )

        return self.tree[current]

    def query(self, current, total_lower, total_upper, lower, upper):
        """ Se quiere el resultado entre un limite y otro distinto al total del texto pasado
        """
        if total_lower >= lower and total_upper <= upper:
            # Si esta en los limites del arbol
            return self.tree[current]
        if total_lower > upper or total_upper < lower:
            # Si no esta en los limites del arbol, se regresa un Nodo vacio
            return Node()

        # Segmentamos la busqueda a la mitad
        mid = (total_lower + total_upper) // 2

        # Obtenemos el resultado en el segmento que vamos buscando formando el arbol
        return self.get_parent_from_children(
            self.query(2 * current + 1, total_lower, mid, lower, upper),
            self.query(2 * current + 2, mid + 1, total_upper, lower, upper),
        )
        
    def max_bp(self, lower, upper):
        """ Se obtiene el largo total de la cadena mas larga balanceada 
        para un segmento determinado del total del texto pasado
        """
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


