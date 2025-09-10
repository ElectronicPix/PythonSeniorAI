import os

ARCHIVO_PRODUCTOS = "productos.txt"

'''
def leer_productos():
    productos = []
    if os.path.exists(ARCHIVO_PRODUCTOS): #Este archivo existe
        with open(ARCHIVO_PRODUCTOS, "r", encoding="utf-8") as archivo:
            for linea in archivo.readlines():
                if linea:
                    
                    if not linea or linea.startswith("ID#"): #Se salta la primera linea
                        continue

                    if not linea or linea.startswith("AUTO_INCREMENT"):# Se salta la ultima
                        continue

                    _id,nombre,precio,stock = linea.split("#")

                    productos.append({
                        "id": int(_id),
                        "nombre": nombre,
                        "precio": float(precio),
                        "stock": int(stock)
                    })
    return productos
'''

def leer_productos():
    productos = []
    if os.path.exists(ARCHIVO_PRODUCTOS): #Este archivo existe
        with open(ARCHIVO_PRODUCTOS, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            for linea in lineas[1:-1]:
                if linea:
                    
                    _id,nombre,precio,stock = linea.split("#")

                    productos.append({
                        "id": int(_id),
                        "nombre": nombre,
                        "precio": float(precio),
                        "stock": int(stock)
                    })
    return productos

def recuperar_autoIncrement():
    #Leer AUTO_INCREMENT
    with open(ARCHIVO_PRODUCTOS, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()
        ultima_linea = lineas[-1].strip()
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
        archivo.write("AUTO_INCREMENT=0")

def guardar_productos(productos,auto_increment):
    with open(ARCHIVO_PRODUCTOS, "w", encoding="utf-8") as archivo:
        archivo.write("ID#Nombre#Precio#Stock\n")
        for p in productos:
            archivo.write(f"{p['id']}#{p['nombre']}#{p['precio']}#{p['stock']}\n")
        archivo.write(f"AUTO_INCREMENT={auto_increment}")

def mostrar_productos():
    pass

def agregar_producto():
    productos = leer_productos()
    auto_increment = recuperar_autoIncrement()

    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    stock = int(input("Stock: "))

    auto_increment +=1

    productos.append({
        "id": auto_increment,
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    })
    guardar_productos(productos,auto_increment)
    print(f"Producto agregado con exito")



def vender_producto():
    productos = leer_productos()
    auto_increment = recuperar_autoIncrement()

    if not productos:
        print("No hay productos para vender")
        return
    
    id_ = int(input("Ingrese el ID del producto a vender: "))
    cantidad = int(input("Ingrese cantidad: "))

    for p in productos:
        if p["id"] == id_:
            if p["stock"] >= cantidad:
                p["stock"] -= cantidad
                print(f"Venta realizada {cantidad} {p['nombre']}(s)")
            else:
                print("No hay productos stock")
        else:
            print("No hay producto")

    guardar_productos(productos, auto_increment)
    
vender_producto()

def menu():
    while True:
        print("TIENDA DEV SENIOR")
        print("1. Mostrar productos")
        break

if __name__ == "__main__":
    if validar_archivo():
        menu()