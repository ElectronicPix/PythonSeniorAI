import os #Rutas de los archivos

ARCHIVO_PRODUCTOS = "productos.txt"

def leer_productos():
    productos = []
    if os.path.exists(ARCHIVO_PRODUCTOS): # Este archivo existe?
        with open(ARCHIVO_PRODUCTOS, "r", encoding="utf8") as archivo:
            lineas = archivo.readlines()
            for linea in lineas[1:-1]:
                if linea:
                    _id, nombre, precio, stock = linea.split("#")# crea los espacios
                    productos.append({
                        "id": int(_id),
                        "nombre": nombre, 
                        "precio": float(precio), 
                        "stock": int(stock)
                    }) #saltar la primero y la ultima vuelta
                 
    return productos
'''    
    if os.path.exists(ARCHIVO_PRODUCTOS): # Este archivo existe?
        with open(ARCHIVO_PRODUCTOS, "r", encoding="utf8") as archivo:
            for linea in archivo.readlines():
                if linea:
                    if not linea or linea.startswith("ID#"):
                        continue #Salta ID
                    
                    if not linea or linea.startswith("AUTO_INCREMENT"):
                        continue #Salta AUTO
                    
                    _id, nombre, precio, stock = linea.split("#")# crea los espacios
                    productos.append({
                        "id": int(_id),
                        "nombre": nombre, 
                        "precio": float(precio), 
                        "stock": int(stock)
                    }) #saltar la primero y la ultima vuelta
            
    return productos'''
def recuperar_autoIncrement():
    with open(ARCHIVO_PRODUCTOS, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()
        #leer AUTO_INCREMENT
        ultima_linea = lineas[-1].split()
        auto_increment = int(ultima_linea.split("=")[1])
        return auto_increment
    
def validar_archivo():
    if not os.path.exists(ARCHIVO_PRODUCTOS):
        crear_archivo()
        return True
    return True
    
def crear_archivo():
    with open(ARCHIVO_PRODUCTOS, "w", encoding="utf-8") as archivo:
        archivo.write("ID#Nombre#Precio#Stock\n")
        archivo.write("AUTO_INCCREMENT=0")
        
def guaradar_productos(productos, auto_increment):
    with open(ARCHIVO_PRODUCTOS, "w", encoding="utf-8") as archivo:
        archivo.write("ID#Nombre#Precio#Stock\n")
        for p in productos:
            archivo.write(f"{p['id']}#{p['nombre']}#{p['precio']}#{p['stock']}")
        archivo.write(f"AUTO_INCREMENT={auto_increment}")

def mostrar_productos():
    pass

def agregar_producto():
    produtos = leer_productos()
    auto_increment = recuperar_autoIncrement()
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    stock = int(input("Stock: "))
    
    auto_increment +=1 
    
    produtos.append({
        "id": auto_increment,
        "nombre": nombre, 
        "precio": precio, 
        "stock": stock
    })
    guaradar_productos(produtos, auto_increment)
    print("Producto agregado con exito")

def vender_producto():
    productos = leer_productos()
    auto_increment = recuperar_autoIncrement()
    
    if not productos:
        print("No hay productos para vender")
        return

    
    id_ = int(input("Ingrese el ID del produto a vender"))
    cantidad = int(input("Ingrese cantidad: "))
    
    for p in productos:
        if p["id"] == id_:
            if p["stock"] >= cantidad:
                p["stock"] -= cantidad
                print(f"Venta realizada {cantidad} {p['nombre']}(s)")
            else:
                print("No hay produtos stock")
        else: 
            print("No hay producto")
    guaradar_productos(productos, auto_increment)       


def menu():
    while True:
        print("TIENDA DEV SENIOR")
        print("1. Mostrar productos")
        break
    
    
if __name__ == "__main__":
    if validar_archivo():
        menu()