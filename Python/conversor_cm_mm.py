while True:
    cm = float(input("Digite o valor em centímetros: "))
    mm = cm * 10
    print(f"O valor em milímetros é: {mm}")
    
    continuar = input("\n¿Deseas continuar? (s/n): ").lower()
    if continuar != 's':
        print("¡Hasta luego!")
        break
