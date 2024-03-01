arreglo_original=[1,2,3,4,5,6,7,8,9]
print(arreglo_original)
arreglo=[]
for element in arreglo_original:
    arreglo.append(element)

arreglo_invertido=[]

while(arreglo):
    arreglo_invertido.append(arreglo.pop())    

print(arreglo_invertido)
