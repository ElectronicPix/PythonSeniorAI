# Factory

# Permitir que la clase no se instancie exactemente o directamente


class Animal:
    
    def hacer_sonido(self):
        pass
    
class Perro(Animal):
    
    def hacer_sonido(self):
        return "Guau"

class Gato(Animal): # Objeto Gato
    
    def hacer_sonido(self):
        return "Miau"
    
class FabricaHacerSoido:
    
    def crear_sonido(self, Objeto):
        return Objeto()
    
#pato1 = Perro()
#print(pato1.hacer_sonido())
    

FabricaSonido = FabricaHacerSoido() 
#print(FabricaHacerSoido.crear_sonido(Gato).hacer_sonido()) sin el self
#print(FabricaHacerSoido.crear_sonido(Perro).hacer_sonido()) sin el self
print(FabricaSonido.crear_sonido(Perro).hacer_sonido())
print(FabricaSonido.crear_sonido(Gato).hacer_sonido())

# 1 h - 03 min - 20 s