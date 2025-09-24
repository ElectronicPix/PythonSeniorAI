class Volador:
    
    def __init__(self, altura):
        self.altura = altura
    
    
    def volar(self):
        return "Pueder volar"
    
    
class Corredor:
    
    def __init__(self, velocidad):
        self.velocidad = velocidad
    
    def correr(self):
        return "Puede camiar"
    

class Nadador:
    
    def __init__(self, profundidad):
        self.profundidad = profundidad
    
    def nadar(self):
        return "Puede nadar"
    

class Perro(Corredor):
    pass

class Pato(Volador, Corredor, Nadador):
    pass


pato1 = Pato(2)# Hereda restricciones 
print(pato1.altura)