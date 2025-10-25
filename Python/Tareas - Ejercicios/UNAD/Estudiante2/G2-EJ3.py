class Empleado:
    def __init__(self, nombre:str, salario:float):
        self.__nombre = nombre
        self.__salario = salario
        
    @property    
    def nombre(self) -> str:
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre_nuevo: str):
        self.__nombre = nombre_nuevo
        
    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, salario_nuevo):
        if salario_nuevo > self.__salario:
            self.__salario = salario_nuevo
        else:
            print(f"❌ Error: El nuevo salario (${salario_nuevo:,.2f}) debe ser mayor que el actual (${self.__salario:,.2f}).")
        
        
    def __str__(self):
        """Representación en string del objeto Empleado."""
        return f"Empleado: {self.nombre}, Salario: ${self.salario:,.2f}"
    
    
    
# --- Ejemplo de uso ---

# 1. Creamos una instancia de la clase Empleado
empleado1 = Empleado("Carlos Gutierrez", 75000.00)
print(empleado1)
print("-" * 20)

# 5. Modificamos el nombre
print("Cambiando el nombre...")
empleado1.nombre = "Carlos Alberto Gutierrez"
print(empleado1)