# Ejemplo clase persona
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre # Atributo
        self.edad = edad     #Atributo
        self.ciudad = "Madrid" # Atributo con valor por defecto.

#crear objeto (instancias)
persona1 = Persona("Ana", 25)
persona2 = Persona("Carlos", 30)

print(persona1.nombre)  #Ana
print(persona2.edad) #30


Atributos = "Marca, color, velocidadActual"
Metodos = "Frenar(), Acelerar(), encender()"
__init__ = "Inicializa la clase"