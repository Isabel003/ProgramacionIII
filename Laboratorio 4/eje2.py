class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):  # Añadir elemento a la cola
        self.items.append(item)

    def dequeue(self):  # Eliminar y devolver el primer elemento de la cola
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None  # Devuelve None si la cola está vacía

    def front(self):  # Ver el primer elemento de la cola sin eliminarlo
        if not self.is_empty():
            return self.items[0]
        else:
            return None  # Devuelve None si la cola está vacía

    def is_empty(self):  # Verificar si la cola está vacía
        return len(self.items) == 0


def proceso_atencion(fila):
    print("Iniciando proceso de atención en la fila...")
    while not fila.is_empty():
        print("Atendiendo al cliente:", fila.dequeue())
    print("Todos los clientes han sido atendidos.")


def main():
    fila = Queue()  # Crear una fila

    # Agregar clientes a la fila
    fila.enqueue("Cliente 1")
    fila.enqueue("Cliente 2")
    fila.enqueue("Cliente 3")
    fila.enqueue("Cliente 4")

    print("Primer cliente en la fila:", fila.front())  # Mostrar el primer cliente en la fila

    proceso_atencion(fila)  # Simular el proceso de atención en la fila


if __name__ == "__main__":
    main()
