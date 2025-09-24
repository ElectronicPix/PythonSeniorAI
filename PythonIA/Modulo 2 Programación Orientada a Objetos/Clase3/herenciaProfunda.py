class Animal:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    
    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"
    

class Canino(Animal):
    def __init__(self, nombre, edad, tiempoVida):
        super().__init__(nombre, edad)
        self.tiempoVida = tiempoVida
        

class Perro(Canino):
    def __init__(self, nombre, edad, tiempoVida, raza):
        super().__init__(nombre, edad, tiempoVida)
        self.raza = raza
        
    
    
perro1 = Perro("Cony", 2, 24, "Criollo")
print(perro1.mostrar_info())



# Polimorfismo override: Sobre escribir la clase
# Polimorfiamo Overload: Sobre carga, multiples metodos con mismo nombre pero diferente parametro
# Polimorfismo Duck type: Camina como pato, suena como pato es un pato