
class Alumno:

    def __init__(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota

    def imprimir(self):
        print(f'El alumno {self.nombre} sacó un {self.nota}')

    def aprobado(self):
        return self.nota>5
        

# nombre=input('Ingrese el nombre del alumno:')
# nota=int(input('Ingrese la nota:'))
# alumno1=Alumno(nombre,nota)
# nombre=input('Ingrese el nombre del alumno:')
# nota=int(input('Ingrese la nota:'))
# alumno2=Alumno(nombre,nota)
alumnos=[]
for i in range(6):
    nombre=input('Ingrese el nombre del alumno:')
    nota=int(input('Ingrese la nota:'))
    alumnos.append(Alumno(nombre,nota))

for alumno in alumnos:
    alumno.imprimir()


    
