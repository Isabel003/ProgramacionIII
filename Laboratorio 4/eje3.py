class Stack:
    def __init__(self):
        self.items = []

    def push(self, item): # Método para añadir elementos a la pila# Método para añadir elementos a la pila
        self.items.append(item)

    def pop(self): # Método para eliminar y devolver el elemento superior de la pila
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0


def paréntesis_balanceados(cadena):
    pila = Stack()  # Crear una pila para rastrear los paréntesis

    for carácter in cadena:
        if carácter == '(':
            pila.push(carácter)  # Si es un paréntesis de apertura, añadirlo a la pila
        elif carácter == ')':
            if pila.is_empty():
                return False  # Si se encuentra un paréntesis de cierre y la pila está vacía, los paréntesis no están balanceados
            else:
                pila.pop()  # Si es un paréntesis de cierre, sacar el paréntesis de apertura correspondiente de la pila

    return pila.is_empty()  # Los paréntesis están balanceados si la pila está vacía al final


if __name__ == "__main__":
    cadena1 = "()()()()((()))"  # Paréntesis balanceados
    cadena2 = "((())"  # Paréntesis no balanceados

    if paréntesis_balanceados(cadena1):
        print(f"Los paréntesis en '{cadena1}' están balanceados.")
    else:
        print(f"Los paréntesis en '{cadena1}' no están balanceados.")

    if paréntesis_balanceados(cadena2):
        print(f"Los paréntesis en '{cadena2}' están balanceados.")
    else:
        print(f"Los paréntesis en '{cadena2}' no están balanceados.")
