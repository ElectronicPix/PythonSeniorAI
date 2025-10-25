class Producto:
    def __init__(self, precio:float):
        self.__precio = precio
        
    def get_precio(self):
        return self.__precio
    
    def set_precio(self, nuevo_precio):
        if nuevo_precio >= 0:
            self.__precio = nuevo_precio
        else:
            print("❌ El precio no puede ser negativo")
    
    def aplicar_descuento(self, porcentaje):
        if 0 <= porcentaje <= 100:
            descuento = self.get_precio() * (porcentaje/100)
            nuevo_precio = self.get_precio() - descuento
            self.set_precio(nuevo_precio)
        else: 
            print("Error: El porcentaje de descuento debe estar entre 0 y 100.")
            


# --- Ejemplo de uso ---

# 1. Creamos una instancia de Producto con un precio inicial de 100
mi_producto = Producto(100)
print(f"Precio inicial: ${mi_producto.get_precio()}")

# 2. Aplicamos un descuento del 20%
print("\nAplicando un descuento del 40%...")
mi_producto.aplicar_descuento(40)
print(f"Precio con descuento: ${mi_producto.get_precio()}")

# 3. Intentamos establecer un precio negativo (mostrará un error)
print("\nIntentando poner un precio negativo...")
mi_producto.set_precio(-45)
print(f"Precio actual: ${mi_producto.get_precio()}")

# 4. Establecemos un nuevo precio válido
print("\nEstableciendo un nuevo precio de 200...")
mi_producto.set_precio(200)
print(f"Precio actualizado: ${mi_producto.get_precio()}")