class Node:
    def __init__(self, valor):
        self.valor = valor
        selfizquierdo= Node
        selderecho = Node

raiz = Node(1)
raiz.izquierdo = Node(2)
raiz.derecha = Node (3)
raiz.izquierdo.izquierdo = Node(4)
raiz.izquierdo.izquierdo.izquierdo= Node(5)
      
