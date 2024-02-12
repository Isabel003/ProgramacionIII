class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):  # Método para añadir elementos a la pila
        self.items.append(item)

    def pop(self):  # Método para eliminar y devolver el elemento superior de la pila
        if not self.is_empty():
            return self.items.pop()
        else:
            return None  # Devuelve None si la pila está vacía

    def peek(self):  # Método para ver el elemento superior de la pila sin eliminarlo
        if not self.is_empty():
            return self.items[-1]
        else:
            return None  # Devuelve None si la pila está vacía

    def is_empty(self):  # Método para verificar si la pila está vacía
        return len(self.items) == 0


def reverse_list(input_list):
    stack = Stack()  # Crear una instancia de la clase Stack
    for item in input_list:  # Recorrer la lista original
        stack.push(item)  # Añadir cada elemento a la pila

    reversed_list = []  # Crear una lista para almacenar los elementos invertidos
    while not stack.is_empty():  # Mientras la pila no esté vacía
        reversed_list.append(stack.pop())  # Sacar elementos de la pila y añadirlos a la lista invertida

    return reversed_list  # Devolver la lista invertida


lista_original = [1, 2, 3, 4, 5]
lista_invertida = reverse_list(lista_original)  # Invertir la lista original utilizando la función reverse_list
print("Lista original:", lista_original)  # Imprimir la lista original
print("Lista invertida:", lista_invertida)  # Imprimir la lista invertida
