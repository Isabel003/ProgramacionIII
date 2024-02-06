
class Estudiante:
    def __init__(self, nombre, edad, calificacion) :
        self.nombre = nombre
        self.edad = edad
        self.calificacion = calificacion
    def aprobado(self):
        if self.calificacion >= 60:
            return True
        else:      
            return False
        
        
nombreEstudiante=input("Ingrese el nombre del estudiante: ")
edadEstudiante=int(input("Ingrese la edad del estudiante: "))
calificacionEstudiante=int(input("Ingrese la calificacion del estudiante: "))
estudiante1=Estudiante(nombreEstudiante, edadEstudiante, calificacionEstudiante)
if estudiante1.aprobado():
    print (estudiante1.nombre, "ha aprobado ")
else: 
    print(estudiante1.nombre, "no ha aprobado ")