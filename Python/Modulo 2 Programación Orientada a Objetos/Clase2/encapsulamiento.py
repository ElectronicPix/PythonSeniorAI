class Persona:

    def __init__(self, nombre: str, edad: int): # Clase reservada, self permite usar las variables dentro de la clase 
        
        #Instancia: Donde se almacena los atributos
        self.__nombre = nombre # Atributo privado: a travez de una clase
        self._edad = edad #Atributo protegido: no permite cambiar 
        self.ciudad = "Bogotá" #Predefinido publico
        
    #Acción - Método
    def saludo(self):
        print(f"Hola mi nombre es {self.__nombre} y mi edad es {self._edad} años")
        
    def get_nombre(self):
        return self.__nombre 
        
persona2 = Persona('Rubén', 24)
print(f"La edad es: {persona2._edad}")
print(persona2.get_nombre())
persona2.saludo()