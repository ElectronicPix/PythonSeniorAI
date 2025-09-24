from abc import ABC, abstractmethod


class Forma(ABC):
    
    # El hijo debe sobre escribirlo
    @abstractmethod
    def calcularArea(self):
        return "No deberías estar aqui"
    
class Rectangulo(Forma):
    pass

class Triangulo(Forma):
    
    def calcularArea(self):
        return "Estoy calculando el área"
    
    
#forma1 = Rectangulo()
#print(forma1.calcularArea())

forma2 = Triangulo()
print(forma2.calcularArea())
