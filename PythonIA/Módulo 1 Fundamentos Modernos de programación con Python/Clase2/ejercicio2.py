'''Universida - Promedio Ponderado'''

#declarar variables y pedir datos por consola
print("Ingrese las notas del estuudiante")
nota1 = float(input("primera nota: "))
nota2 = float(input("Segunda nota: "))
nota3 = float(input("Tercera nota: "))

#aplcación de operadores

nota1 *= 0.30
nota1 *= 0.30
nota1 *= 0.40

#no se divide por que ya se aplicaron los porcentajes.
promedio = nota1 + nota2 + nota1

#salida  de datos por consola

print(f"el promedio fial es: {promedio:.2f}")

