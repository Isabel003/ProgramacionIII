class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0
    
    
    def __len__(self):
        return len(self.items)


def reverse_half_queue(queue):
    stack = []

    # Movemos la mitad de los elementos de la cola a la pila
    half_size = len(queue) // 2
    for _ in range(half_size):
        stack.append(queue.dequeue())

    # Movemos los elementos de la pila de vuelta a la cola, invirtiendo su orden
    while stack:
        queue.enqueue(stack.pop())

    # Rotamos los elementos restantes de la cola para mantener la secuencia
    for _ in range(half_size):
        queue.enqueue(queue.dequeue())


if __name__ == "__main__":
    cola = Queue()

    # Agregamos elementos a la cola para el ejemplo
    for i in range(1, 11):
        cola.enqueue(i)

    print("Cola antes: ", cola.items)

    reverse_half_queue(cola)

    print("Cola después: ", cola.items)
