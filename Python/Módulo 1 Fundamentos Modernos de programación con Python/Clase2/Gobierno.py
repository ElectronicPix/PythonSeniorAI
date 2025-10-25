"""
        el gobinerno dara insentivos economicos a la problación dependiendo el estrato
        - estrato 1 : 1 millon de pesos
        - estrato 2 : 500 mil pesos
        - estrato 3 : 200 mil pesos
        - estrato 4 : 0 pesos
        - estrato 5 : impuesto de 300 mil pesos
        - estrato 6 : inpuesto 600 mil pesos 
        - estratos mayores a 6 : Error
        - esrtato menores a 0 : Error 
        Dinero solo aplicado para el pago de matricula de la Universidad
"""

#declaración de varibales y entrada de datos

estrato = int(input("digite el estrato: "))
valorMatricula = float(input("digite el valor de la matricula: "))

#implementacion de condicionales

if(estrato == 1):
    valorMatricula -= 1000000
    print(f"el valor de la matricula es: {valorMatricula:.0f}")
elif (estrato == 2):
    valorMatricula -= 500000
    print(f"el valor de la matricula es: {valorMatricula}")
elif (estrato == 3):
    valorMatricula -= 200000
    print(f"el valor de la matricula es: {valorMatricula}")
elif (estrato == 4):
    print(f"el valor de la matricula es: {valorMatricula}")
elif (estrato == 5):
    valorMatricula += 300000
    print(f"el valor de la matricula es: {valorMatricula}")
elif (estrato == 6):
    valorMatricula += 600000
    print(f"el valor de la matricula es: {valorMatricula}")
else:
    print("el estrato no existe (Error)")