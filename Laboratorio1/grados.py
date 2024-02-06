
def celsiusAfah(celsius):
   fahrenheit = ((celsius* 9/5)+32)
   return fahrenheit

celsius=float(input("Ingrese grados Celsius: "))
fahrenheit = celsiusAfah(celsius)
print (f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")



