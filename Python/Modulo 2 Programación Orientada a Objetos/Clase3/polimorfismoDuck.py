class Nadador:
    def __init__(self, nadar):
        self.nadar = nadar
        

##########################################################


class Pato:
    
    def nadar(self):
        return "El pato nada en el agua"
    
class Barco:
    
    def nadar(self):
        return "El barcoo nada en el agua"
        
        
class Pez:
    
    def nadar(self):
        return "El pez nada en el agua" 


def procesar_objeto_acuatico(objeto):
    return objeto.nadar()


pato1 = Pato()
barco1 = Barco()
pez1 = Pez()

print(procesar_objeto_acuatico(pez1))