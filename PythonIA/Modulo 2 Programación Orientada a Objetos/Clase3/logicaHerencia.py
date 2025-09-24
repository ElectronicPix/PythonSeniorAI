class Animal:
    
    def hace_sonido(self):
        pass
    
class Perro(Animal):
    pass

# Esta mal por que motor no es un tipo de coche. Coche -> Motor. Motor  no es un coche
class Motor:
    
    def arrancar(self):
        return "Motor arrancar"
    
class Coche(Motor):
    pass



class Coche2:
    
    def __init__(self):
        self.motor = Motor() # Un coche tiene un motor, no hereda un motor 