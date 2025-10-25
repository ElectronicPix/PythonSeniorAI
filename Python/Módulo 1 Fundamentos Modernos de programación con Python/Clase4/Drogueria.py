"""
    la drogueria solo maneja 3 productos fijos en el sistema. cada uno tiene su propio nombre, 
    precio e ingreso acumulado. El usuario podra:
    
    Ver los producto disponibles
    Vender cualquiera de los 3 productos
    Consultar igresos totales 
    Salir del sistema
    
    """
    
#Pedir los 3 productos

p1 = "acetaminofen"
precio1 = 2000
ingreso1 = 0

p2 = "ibuprofeno"
precio2 = 3500
ingreso2 = 0

p3 = "omeprasol"
precio3 = 6700
ingreso3 = 0


def mostraMenu():
    print("\n Menu drogueria")
    print("1. Ver productos dispobiles")
    print("2. Vender producto")
    print("3. Mostrar ingresos totales")
    print("4. Salir")
    
def verProducto():
    print("\n productos disponibles")
    print(f"1. {p1} - {precio1}") 
    print(f"2. {p2} - {precio2}") 
    print(f"3. {p3} - {precio3}") 
    
def venderProducto():
    global ingreso1, ingreso2, ingreso3 #Variables globales
    
    verProducto()
    
    opcion = int(input("Seleccione el numero del producto a vender: "))
    if opcion == 1:
        cantidad = int(input(f"cuantos {p1} desea vender: "))
        total = cantidad * precio1
        ingreso1 += total
        print(f"venta realizada por ${total}")
    
    elif opcion == 2:
        cantidad = int(input(f"cuantos {p2} desea vender: "))
        total = cantidad * precio1
        ingreso2 += total
        print(f"venta realizada por ${total}")
    
    elif opcion == 3:
        cantidad = int(input(f"cuantos {p3} desea vender: "))
        total = cantidad * precio1
        ingreso3 += total
        print(f"venta realizada por ${total}")
    
    else:
        print("opcion no valida")
        

def mostrarIngresos():
    totalIngresos = ingreso1 + ingreso2 + ingreso3
    print(f"Total general e igual: ${totalIngresos}")
    

while True:
    mostraMenu()
    opcion = int(input("Seleccione una opcion: "))
    if opcion == 1:
        verProducto()
    elif opcion == 2:
        venderProducto()
    elif opcion == 3:
        mostrarIngresos()
    elif opcion == 4:
        print("gracias por  usar el sistema")
        break
    else:
        print("opcion no valida")