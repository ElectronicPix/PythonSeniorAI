class Empleado:
    
    def __init__(self, nombre, apellido, cedula):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        
        
    def mostrar_info(self):
        return f"Mostrar información del empleado: {self.nombre}, {self.apellido}, {self.cedula}"
    
class MedioTiempo(Empleado):
    
    def __init__(self, nombre, apellido, cedula, tipoContrato):
        super().__init__(nombre, apellido, cedula) # Herencia padre
        self.tipoContrato = tipoContrato # Nuevo atributo
        
        

class PorHoras(Empleado):
    
    def __init__(self, nombre, apellido, cedula, horasTrabajadas):
        super().__init__(nombre, apellido, cedula)
        self.horasTrabajadas = horasTrabajadas
        
    # Polimorfismo Sobrescritura (Override)
    def mostrar_info(self):
        #return f"super().mostrar_info(), {self.horasTrabajadas}"
        return f"Mostrar información del empleado: {self.nombre}, {self.apellido}, {self.cedula}, {self.horasTrabajadas}"
        

empleadoPorHoras =  PorHoras("Juan", "Triana", 1002, 25)
print(empleadoPorHoras.mostrar_info())

empleadoMedioTiempo = MedioTiempo("Juan", "Triana", 1002, True)
print(empleadoMedioTiempo.mostrar_info())