"""saldo = 5.000

while True:
    print("\n ----MENU----")
    print("1. Ver saldo")
    print("2. Retirar dinero")
    print("3. Salir")
    
    opcion = int(input("Digite la opcion: "))
    
    if opcion == 1:
        print(f"su saldo actual es: {saldo:.3f}")
    elif opcion == 2:
        retiro = float(input("cuanto deseas retirar? "))
        if retiro <= saldo:
            saldo -= retiro
            print(f"Retiro exitoso. Saldo restante ${saldo:.3f}")
        else:
            print("Saldo insificiente")
    elif opcion == 3:
        print("gracias por usar nuestro sistema")
        break # detiene el programa
    else:
        print("Opcion invalida")"""
        
        
'''Comandos'''
# Alt + Shit + flecha abajo
# Windows + .


historial = []
saldo = 5.000

clave = 'admin'

while True:
    print("\n ----MENU----")
    print("1. Ver saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Ver historial movimientos")
    print("5. Cambiar clave")
    print("6. Salir")
    
    
    opcion = int(input("Digite la opcion: "))
    
    if opcion == 1:
        print(f"su saldo actual es: {saldo:.3f}")
        
    elif opcion == 2:
        monto = float(input("cuanto deseas retirar? "))
        if monto <= saldo:
            saldo -= monto
            historial.append(f"Retiraste {monto:.3f}")
            print(f"Retiro exitoso. Saldo restante ${saldo:.3f}")
        else:
            print("Saldo insificiente")
            
    elif opcion == 3:
        monto = float(input("Cuanto desea depositar? "))
        if monto > 0:
            saldo += monto
            historial.append(f"Depositaste {monto:.3f}")
            print(f"Deposito exitoso. Nuevo saldo {saldo:.3f}")
        else:
            print("No puede depositar monto negativo")
            
    elif opcion == 4:
        print("---- Historial----")
        if len(historial) == 0:
            print("No tienes movimientos")
        else:
            for movimiento in historial:
                print(movimiento)
                
    elif opcion == 5:
        intento = input("Escribe tu clave actual: ")
        if intento == clave:
            nueva = input("Escribe tu nueva clave: ")
            clave = nueva
            print("Tu clave ha sido cambiada con exito")
        else:
            print("Clave incorrecta")
    elif opcion == 6:
        print("gracias por usar nuestro sistema")
        break
    else:
        print("Opcion invalida")
        
        
        

#colecciones
