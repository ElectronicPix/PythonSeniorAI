#from ..models import estudiante
#from ..models import matricula
#from ..models import programa

from models.estudiante import Estudiante
from models.programa import Programa


class ControllerEstudiantes:
    
    def __init__(self):
        self.estudiantes = []
    
    def agregarEstudiante(self, estudiante: Estudiante): #object
        for estudiantes in self.estudiantes:
            if (estudiantes.documento == estudiante.documento) or (estudiantes.email == estudiante.email):
                return False
        self.estudiantes.append(estudiante)
        return True
    
    def mostrarEstuadiante(self):
        for estudiante in self.estudiantes:
            return estudiante
    
    def mostrarEstudiantePorDocuemnto(self, documento):
        for estudiante in self.estudiantes:
            if estudiante.documento == documento:
                return estudiante
            
    def mostraEstudiantePorEmail(self, email):
        for estudiante in self.estudiantes:
            if estudiante.email == email:
                return estudiante
            
    def actualizarEstudiante(self, documento, nombre, apellido):
        for estudiantes in self.estudiantes:
            if estudiantes.documento == documento:
                estudiantes.nombre == nombre
                estudiantes.apellido == apellido
                return True
            
    def eliminarEstudiante(self, documento):
        for estudiantes in self.estudiantes:
            if estudiantes.documento == documento:
                self.estudiantes.remove(estudiantes)
                return True

class ControllerPrograma:
    def __init__(self):
        self.Programas = []
        
    def agregarPrograma(self, programa: Programa):
        pass


#prueba
""" ce = ControllerEstudiantes()
estudiante_nuevo = Estudiante(1, '12345678', 'Andres', 'Paniza', 'andres@gmail.com')
ce.agregarEstudiante(estudiante_nuevo)
ce.mostrarEstuadiante() """