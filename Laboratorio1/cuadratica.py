import math

def ecuacion (a,b,c):
    d= b**2 -4*a*c
    if d >=0:
        x1 =(-b +math.sqrt(d))/(2*a)
        x2 =(-b -math.sqrt(d))/(2*a)
        return x1, x2
    else:
        return None
    
a=float(input("Ingresar el coeficiente a: "))
b=float(input("Ingresar el coeficiente b: "))
c=float(input("Ingresar el coeficiente c: "))

resultado= ecuacion(a,b,c)

if resultado is not None:
    print(f"Las soluciones son x1 = {resultado[0]} y x2 = {resultado[1]}")
else:
    print("La ecuación no tiene soluciones reales.")