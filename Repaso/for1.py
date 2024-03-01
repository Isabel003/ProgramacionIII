#suma de de numeros

n=int(input("Igrese un numero: "))
suma=0
for i in range(1,n+1):
    suma=suma+i
print (f"Suma de todos los numeros del 1 al {n}, es {suma}")