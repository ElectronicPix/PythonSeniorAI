for i in range(0, 3): #imprime del 0 - 2
    print(i)
    
    
frutas = ['manzana', 'pera', 'fresa']

for fruta in frutas:
    print(fruta)
    


#while se inicializa por fuera
contador = 1 

while contador <= 5:
    print(contador)
    contador += 1
    
    
    
suma = 0

numero = int(input("Ingrese el numero: "))

while numero != 0:
    suma += numero
    numero = int(input("Ingrese el numero: "))
    
print(f"la suma total es: {suma}")