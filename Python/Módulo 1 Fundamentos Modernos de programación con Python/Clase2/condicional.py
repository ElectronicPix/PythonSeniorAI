'''
Cuando la salida de un proceso tiene más de un resultado posible se debe tomar decisiones.
más de un posible resultado.

if(condicion): # if normal tiene dos caminos de solución
    INSTRUCCIONES
    
elif(condicion):
    INSTRUCCIONS
    
else: #Negacion de las condiciones que no se cumplieron
    INSTRUCCIONES

'''

numero = int(input("digite el numero: "))

#tomar decisiones (condicionales) - estructuras de control

'''if (numero >= 0):
    print(f"el {numero} es positivo")
else:
    print(f"el {numero} es negativo")
'''

if(numero == 0):
    print(f"el {numero} es nulo")
elif(numero > 0):
    print(f"el {numero} es positivo")
else:
    print(f"el {numero} es negativo")  

