""" Ejercicio 1: Clase Persona 

Planteamiento 

Crear una clase Persona, con atributos Nombre y Edad. Crear un método que muestre un saludo. 


Pseudocódigo

Clase Persona:
    
    Atributos: nombre, edad
    
    Metodo saludar():
        
        Imprimir "Hola, soy {nombre} y tengo {edad} años." """
        
        
class Persona:
    
    def __init__ (self, nombre, edad):
        
        self.nombre = nombre
        self.edad = edad
        
    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")
        

persona1 = Persona("Carlos", 30)
persona2 = Persona("Ruben", 25)
persona3 = Persona("Juan", 20)



persona1.saludar()