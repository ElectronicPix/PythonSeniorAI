def saludar_persona(nombre, hora):
    if hora < 12:
        print(f"Buenos días, {nombre}")
    elif hora < 18:
        print(f"Buenas tardes, {nombre}")
    else:
        print(f"Buenas noches, {nombre}")
        
        
saludar_persona("Juan", 9)
saludar_persona("Ana", 17)
saludar_persona("Luis", 20)


