class Universidad:
    def __init__(self, nombre="", direccion="", telefono=0):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def get_nombre(self):
        return self.nombre

    def set_nombre(self,nombre):
        return self.nombre
    
    def get_direccion(self):
        return self.direccion

    def set_direccion(self,direccion):
        return self.direccion

    def get_telefono(self):
        return self.telefono

    def set_telefono(self,telefono):
        return self.telefono

    def remove_universidad(self):
        self.nombre=""
        self.direccion=""
        self.telefono=0
        return self.nombre, self.direccion, self.telefono

class Facultad(Universidad):
    def __init__(self, facultad=""):
        self.facultad = facultad
        Universidad.__init__(self, facultad)

    def get_facultad(self):
        return self.facultad

    def set_facultad(self,facultad):
        return self.facultad

    def remove_facultad(self):
        self.facultad=""
        return self.facultad

class Estudiante(Universidad):
    def __init__(self, est="",matricula=0):
            self.est = est
            self.matricula = matricula
            Universidad.__init__(self, facultad)

    def get_estudiante(self):
        return self.est

    def set_estudiante(self,est):
        return self.est

    def get_matricula(self):
        return self.matricula

    def set_matricula(self,matricula):
        return self.matricula


class Profesor(Facultad):
    def __init__(self, prof="",id=0):
            self.prof = prof
            self.id = id
            Facultad.__init__(self,facultad)

    def get_profesor(self):
        return self.prof

    def set_profesor(self,prof):
        return self.prof

    def get_id(self):
        return self.id

    def set_id(self,id):
        return self.id

class Semestre(Estudiante):
    def __init__(self, numero=0):
            self.numero = numero
            Estudiante.__init__(self,estudiante)

    def get_semestre(self):
        return self.numero

    def set_semestre(self,numero):
        return self.numero

class Grupo(Estudiante):
    def __init__(self, gpo=0):
        self.gpo = gpo
        Estudiante.__init__(self,estudiante)

    def get_grupo(self):
        return self.gpo

    def set_grupo(self,gpo):
        return self.gpo

class Materia:
    def __init__(self, mat="", clave=0):
        self.mat = mat
        self.clave = clave

    def get_materia(self):
        return self.mat

    def set_materia(self,mat):
        return self.mat

    def get_clave(self):
        return self.clave

    def set_clave(self,clave):
        return self.clave

class Examenes(Materia):
    def __init__(self, num_exam=0):
        self.num_exam = num_exam
        Materia.__init__(self,materia)

    def get_examen(self):
        return self.num_exam

    def set_examen(self,num_exam):
        return self.num_exam

class Calificaciones(Examenes):
    def __init__(self, calif=0):
        self.calif = calif
        Examenes.__init__(self,materia)

    def get_calificacion(self):
        return self.calif

    def set_calificacion(self,calif):
        return self.calif
    
universidad = Universidad("Universidad Autonoma de Baja California","Calz.Tecnologico",6648578789)
facultad = Facultad("Ciencias Quimicas e Ingenieria")
profesor = Profesor("Manuel Castañon Puga")
estudiante = Estudiante("Andres Navarrete Perez",1284707)
semestre = Semestre(3)
grupo = Grupo(532)
materia = Materia("Lenguaje de programacion Python")
examen1 = Examenes(1)
calificacion = Calificaciones(80)
print(f"El estudiante {estudiante.get_estudiante()}  de matricula {estudiante.get_matricula()}")
print(f"perteneciente a la facultad {facultad.get_facultad()}")
print(f"de la universidad {Universidad.get_nombre()} localizada en {Universidad.get_direccion()};")
print(f"esta cursando la materia {materia.get_materia()} del semestre {semestre.get_semestre()}")
print(f"en el grupo {grupo.get_grupo()} con la profesora {profesor.get_profesor()};")
print(f"en el examen {examen1.get_examen()} obtuvo un {calificacion.get_calificacion()} de calificacion")