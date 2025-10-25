def tablaMultiplicar(numero):
    for i in range(1, 11):
        print(f"{numero}  x  {i} = {numero * i}")
        
#tablaMultiplicar(5)

numero = int(input("Ingresa el numero: "))
tablaMultiplicar(numero)