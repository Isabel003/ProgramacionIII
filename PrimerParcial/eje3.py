#Escribe un programa que pida al usuario una lista de números y luego imprima la suma de los números pares en la lista.

numeros = input("Ingresa una lista de numeros separados por espacios: ")

lista_nums = numeros.split()
lista_nums = [int(i) for i in lista_nums]


suma_pares = 0

for num in lista_nums:
    
    if num % 2 == 0:
        suma_pares += num

print("La suma de los numeros pares en la lista es:", suma_pares)

