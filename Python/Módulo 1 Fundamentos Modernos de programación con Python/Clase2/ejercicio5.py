""" Fábrica - Comparación de Producción"""

#declarar variables y perdir datos por consola

print("Ingrese la producción por cada turno")

turno1 = float(input("Producción turno 1: "))
turno2 = float(input("Producción turno 2: "))

#implementamos operadores

diferencia = turno1 - turno2

print(f"la diferencia de producción es: {diferencia}")
print("si el número es positivo, el turno 1 tuvo mayor producción")
print("si el número es negativo, el turno 2 tuvo mayor producción")
print("si el numero es 0, ambos turnos produjeron igual")