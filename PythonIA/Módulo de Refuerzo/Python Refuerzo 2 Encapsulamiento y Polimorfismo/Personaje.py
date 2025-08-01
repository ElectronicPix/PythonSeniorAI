class Personaje:  
    """
    Self: Permite acceder a los atributos y métodos de la instancia actual
        de la clase, hace referencia a recibir el objeto.
        Si el self no se declara en el init, resulta(AttributeError)
    """
    def __init__(self, vida, daño, defensa): 
        self.vida = vida
        self.daño = daño
        self.defensa = defensa


    #métodos especiales    
    def __new__(): #Se ejecuta por debajo, antes que se invoque el init
        pass
     
guerrero1 = Personaje(100, 10, 5)
#Procedimiento. Python invoca primero a new y luego pasa el objeto vacio a __init__
#New crea el objeto vacio y el init se encarga de dar las caracteristicas
#Tipos de métodos: instancia, clase(@classmethod), estaticos(@staticmethod).



#Decoradores

#Para el método clase se usa cls
@classmethod
def funcio(cls):
    pass

#Método estatico
@staticmethod
def funcion_estatica():
    pass

#Método instancia
def mi_metodo(self, nombre):
    print(f"Hola,{nombre}")

mi_metodo()





#Metodos especiales para la herencia
#print(Guerrero.__bases__) #Indica de quien hereda, quien es el padre de guerrero
#print(Personaje.__subclasses__()) #Personaje transmite su herencia a ....
#print(Personaje.__mro__) #Devuelve el orden o jerarquia de herencia

"""
    __bases__:

    ¿Qué es? Es un atributo especial de una clase que devuelve una tupla con todas las clases base directas (padres) 
    de las que hereda.
    Ejemplo: Guerrero.__bases__ te dirá que Guerrero hereda directamente de Personaje.
   
    __subclasses__():

    ¿Qué es? Es un método que, al ser llamado desde una clase, devuelve una lista de todas las clases 
    que heredan directamente de ella (sus "hijas").
    Ejemplo: Personaje.__subclasses__() buscará en todo el código ejecutado y te mostrará una lista que incluye a la clase Guerrero.
   
    __mro__ (o el método mro()):

    ¿Qué es? Significa Method Resolution Order (Orden de Resolución de Métodos). 
    Es un atributo que devuelve una tupla con la jerarquía de clases, en el orden en que Python las recorrerá para buscar 
    un método o atributo. El orden siempre incluye la propia clase al principio y termina con la clase base object.
    Ejemplo: Guerrero.__mro__ te mostrará el orden (Guerrero, Personaje, object). Esto significa que si llamas a un 
    método en un objeto Guerrero, Python lo buscará primero en Guerrero, luego en Personaje y finalmente en la clase object 
    (la madre de todas las clases en Python).
    
"""