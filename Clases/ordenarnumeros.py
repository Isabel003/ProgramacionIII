entrada_usuario = input("Ingrese los numeros a ordenar separados por espacios: ")
lista_de_numeros = [float(x)for x in entrada_usuario.split()]
lista_de_numeros.sort()
print(lista_de_numeros)