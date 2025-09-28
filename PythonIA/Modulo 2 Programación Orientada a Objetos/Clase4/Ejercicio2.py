# Factory

# Permitir que la clase no se instancie exactemente o directamente


class Animal:
    
    def hacer_sonido(self):
        pass
    
class Perro(Animal):
    
    def hacer_sonido(self):
        return "Guau"

class Gato(Animal):
    
    def hacer_sonido(self):
        return "Miau"
    
class FabricaHacerSoido:
    
    def crear_sonido(Objeto):
        return Objeto()
    
pato1 = Perro()
print(pato1.hacer_sonido())
    
    