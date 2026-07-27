# Conversor sencillo de centímetros a milímetros
# El programa solicita un valor en centímetros, lo convierte a milímetros
# y repite hasta que el usuario decida salir.
while True:
    # Leer entrada del usuario y convertir a float (centímetros)
    cm = float(input("Digite o valor em centímetros: "))

    # 1 centímetro = 10 milímetros
    mm = cm * 10

    # Mostrar el resultado en milímetros
    print(f"O valor em milímetros é: {mm}")

    # Preguntar al usuario si desea continuar; 's' (sí) continúa, cualquier
    # otra respuesta terminará el bucle.
    continuar = input("\n¿Deseas continuar? (s/n): ").lower()
    if continuar != 's':
        print("¡Hasta luego!")
        break
