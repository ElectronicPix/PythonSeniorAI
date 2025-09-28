'''Patrones de Diseños'''
# Resetas 

# Patrones de creación
# Patrones de estructura: Trabajar sobre el
# Adapter: Adactar a cualquier situación

class MotorViejo: # Código viejo
    
    def encender(self):
        return "Motor encendido"
    
    
class MotorNuevo:
    def encendido(self):
        return "Motor encendido"
    
class AdaptadorMotor:
    
    def __init__(self, motor):
        self.motor = motor
        
    def encender(self):
        print(self.motor.encendido())
    
    
#motor = MotorViejo()
motor = AdaptadorMotor(MotorNuevo())
motor.encender() # Código viejo 



    

# Open: Abieto a la extensión
# Close: Cerrado a la modificación
