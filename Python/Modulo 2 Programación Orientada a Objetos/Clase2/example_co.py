class Persona:
    '''
    param:
    nombre(str): nombre del usuario
    edad(int): edad usuario
    
    metodos:
    saludar: imprime un saludo
    '''
    def __init__(self, nombre: str, edad: int): # Clase reservada, self permite usar las variables dentro de la clase 
        
        #Instancia: Donde se almacena los atributos
        self.nombre = nombre # Atributo 
        self.edad = edad #Atributo 
        self.ciudad = "Bogotá" #Predefinido
        
        
    #Acción - Método
    def saludo(self):
        print(f"Hola mi nombre es {self.nombre} y mi edad es {self.edad} años")
        
        
        
persona1 = Persona('Rubén', 25)
persona1.saludo()



