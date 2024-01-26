horas = int(input("Ingrese la hora: "))
minutos = int(input("ingrese los muinutos: "))
segundos = int (input("Ingrese los segundos: "))

segTranscurridos= horas*3600 + minutos *60 + segundos
print (f"Han transcurrido en el dia {segTranscurridos}")
