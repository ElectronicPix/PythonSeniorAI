def validarPass():
    password = "devsenior"
    intentos = 0
    
    while intentos < 3:
        entrad = input("Ingrese el password: ")
        if entrad == password:
            print("Bienvenido al Home de Dev Senior")
            return 
        else:
            intentos += 1
            print(f"")
    print(f"password incorrecto, tienes {3 - intentos} intentos")
    
    
validarPass()
