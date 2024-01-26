def determinar_tipo_de_dato(valor):
    tipo = type(valor).__name__
    return tipo


x = input("Ingresa un valor: ")

try:
    valor_entero = int(x)
except ValueError:
    valor_entero = None

try:
    valor_flotante = float(x)
except ValueError:
    valor_flotante = None

if valor_entero is not None:
    print(f"Ingresar este valor como un entero.")
elif valor_flotante is not None:
    print(f"Ingresar este valor como un número decimal.")
else:
    print(f"Ingresar este valor como una cadena .")
