#Simulando una linea de espera de un banco

from collections import deque
import  time 

def simular_linea_esperea(clientes):
    queue= deque(clientes)
    while queue:
        print("Atendiendo al cliente", queue.popleft())
        time.sleep(1)
clientes_en_espera =["Cliente 1" ,"Cliente 2", "Cliente 3", "Cliente 4"]

print("Bienvenido al banco, se les estara atendiendo segun este orden")
simular_linea_esperea(clientes_en_espera)
print("Todos los clientes han sido atendidos")