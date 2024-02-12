class ColaConPilas:
    def __init__(self):
        self.pila_entrada = []  # Pila para el proceso de entrada
        self.pila_salida = []   # Pila para el proceso de salida

    def enqueue(self, elemento):
        self.pila_entrada.append(elemento)  # Añadir elementos a la pila de entrada

    def dequeue(self):
        if not self.pila_salida:  # Si la pila de salida está vacía, mover elementos de la pila de entrada a la pila de salida
            while self.pila_entrada:
                self.pila_salida.append(self.pila_entrada.pop())
        if self.pila_salida:  # Si la pila de salida tiene elementos, devolver el elemento de la cima 
            return self.pila_salida.pop()
        else:
            return None  # Devolver None si ambas pilas están vacías

    def is_empty(self):
        return not self.pila_entrada and not self.pila_salida  # La cola está vacía si ambas pilas están vacías


if __name__ == "__main__":
    cola = ColaConPilas()

    cola.enqueue(1)
    cola.enqueue(2)
    cola.enqueue(3)

    print("Elemento extraído:", cola.dequeue())  # La  primera vez que se llama al método debe imprimir 1
    print("Elemento extraído:", cola.dequeue())  # La segunda vez que se llama al método debe imprimir 2

    cola.enqueue(4)

    print("Elemento extraído:", cola.dequeue())  #  La tercera vez que se llama al método debe imprimir 3
    print("Elemento extraído:", cola.dequeue())  #  La cuarta vez que se llama al método debe imprimir 4


    print("La cola está vacía:", cola.is_empty())  # Debería imprimir True
