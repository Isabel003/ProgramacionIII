
valor = input("Ingrese un valor: ")

if valor.isdigit():
    tipo_dato = "entero"
elif valor.replace(".", "", 1).isdigit():
    tipo_dato = "decimal"
else:
    tipo_dato = "cadena"


print("El tipo de dato de la variable es:", tipo_dato)