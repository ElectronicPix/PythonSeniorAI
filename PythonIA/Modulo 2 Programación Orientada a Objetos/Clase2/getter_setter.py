class Persona:

    def __init__(self, nombre: str, edad: int, ciudad: str = "Bogota"): # Clase reservada, self permite usar las variables dentro de la clase 
        
        #Instancia: Donde se almacena los atributos
        self._nombre = nombre 
        self._edad = edad 
        self._ciudad = ciudad
        
        
    @property
    def edad(self):
        return self.edad
        
    @edad.setter
    def edad(self, nueva_edad):
        #self.__edad = nueva_edad
        if nueva_edad > 0:
            self._edad = nueva_edad
        else:
            print("La edad debe ser positiva")
        
    def saludo(self):
        print(f"Hola mi nombre es {self._nombre} y mi edad es {self._edad} años")
        
persona1 = Persona('Rubén', 24, "Ibague")
persona1._edad = 30
persona1.saludo()