class Persona:
    
    def __init__(self, nombre="Javier", edad=23):
        self.nombre = nombre
        self.edad = edad
        
    def saludar(self):
        return f"Hola, {self.nombre}, edad: {self.edad}"
    
persona1 = Persona()
print(persona1.saludar())