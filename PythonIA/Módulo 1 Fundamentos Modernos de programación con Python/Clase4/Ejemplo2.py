def validarPass():
    password = "devsenior"
    intentos = 0
    
    while intentos < 3:
        entrada = input("Ingrese el password: ")
        if entrada == password:
            print("Bienvenido al Home de Dev Senior")
            return 
        else:
            intentos += 1
            print(f"")
    print(f"password incorrecto, tienes {3 - intentos} intentos")
    
    
validarPass()
