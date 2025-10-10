''' Cadena de responsabilidad: Pasar una soliitud a traves de una cadena de objetoos.'''

# Dependen de la situación

class Manejador:
    
    def __init__(self, siguiente=None):
        self.siguiente = siguiente
        
        
    def manejo(self, solicitud):
        if self.siguiente:
            return self.siguiente.manejo(solicitud) 
        return "Solicitud no atendida"
     
class SoporteBasico(Manejador):
    
    def manejo(self, solicitud):
        if solicitud == "Preguntas generales":
            return "Soporte basico respondido"
        return super().manejo(solicitud)
    
class SoporteTecnico(Manejador):
    
    def manejo(self, solicitud):
        if solicitud == "Preguntas tecnicas":
            return "Soporte tecnico respondido"
        return super().manejo(solicitud)
    
class SoporteEspecializado(Manejador):
    
    def manejo(self, solicitud):
        if solicitud == "error critico":
            return "Soporte especializado respondido"
        return super().manejo(solicitud)
    
    
    
cadena = SoporteBasico(SoporteTecnico(SoporteEspecializado())) # Se debe agregar las reponsabilidades nuevas en el mismo orden 

print(cadena.manejo("Preguntas generales"))
print(cadena.manejo("Preguntas tecnicas"))
print(cadena.manejo("error critico"))
print(cadena.manejo("Pregunta rara"))


#chain
#visor
#observer