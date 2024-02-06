def par_impar(x1,x2):
    suma=x1+x2
    return suma %2==0

x1= float(input("Ingrese primer numero: "))
x2=float(input("Ingrese el segundo numero: "))

result= par_impar(x1, x2)
print ("Es par" if result == True else "No es par")

