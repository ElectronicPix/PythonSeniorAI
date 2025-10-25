def menu_opciones():
    print("Tipos de vehiculos")
    print("1. Carro")
    print("2. Moto")
    print("3. Camion")
    print("0. Salir")
    

def pedir_tipo_vehiculo():
    while True:
        menu_opciones()
        opcion = input("Seleccione una opcion (1 - 3): ").strip()
        if opcion == "1":
            return "carro"
        elif opcion == "2":
            return "moto"
        elif opcion == "3":
            return "camion"
        elif opcion == "0":
            return False
        else:
            print("Opcion no valida")
            
            
            
def mostrar_resultados(resultados):
    print(resultados)
    

def despedida():
    print("Gracias por usar el sistema de parqueadero, Hasta pronto")