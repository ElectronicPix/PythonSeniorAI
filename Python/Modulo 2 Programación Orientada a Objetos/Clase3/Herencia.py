class Animal: #Super Clase
    '''Atributos'''
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    '''Métodos'''
    def mostrar_info(self):
        return f"nombre: {self.nombre}, edad: {self.edad}"
    
    
class Perro(Animal): # Subclase, perro hereda de animmal
    '''Constructores'''
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad) # Lllamar constructor padre
        self.raza = raza # Nuevo atributo
    
    def mostrar_info(self):
        return f"{super().mostrar_info()}, raza: {self.raza}" #Polimorfismo: Función heredada y cambiar su comportamiento.
         
         
         
animal = Animal("Generico", 5)
print(animal.mostrar_info())


perro = Perro("Cony", 2, "Criollo")
print(perro.mostrar_info()) # Forma de imprimir la instanciación de la variable.