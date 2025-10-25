"""
    dev senior en el examen de certificaión intermacional del modulo 4, pide 
    que sus alumnos sean calificados por 3 exmanes cada uno con un peso diferente.
    
    ca1 30%
    ca2 40%
    ca3 30%
    
    si su promedio es entre 0 - 2.9 reprueba
    si es etre 3.0 - 5.0 aprueba
    mayor a 5 error
    menor a 0 error
"""

#declarar variables y perdir datos por consola
ca1 = float(input("Digite la calificaión 1: "))
ca2 = float(input("Digite la calificaión 2: "))
ca3 = float(input("Digite la calificaión 3: "))

#implementar operadores 
ca1 *= 0.30
ca2 *= 0.40
ca3 = 0.30

promedio = ca1 + ca2 + ca3

if(promedio >= 0 and promedio < 3):
    print(f"el promedio es {promedio:.2f} por lo tanto reprueba")
elif(promedio >= 3 and promedio <= 5):
    print(f"el promedio es {promedio} por lo tanto aprueba")
else: 
    print(f"el promedio es {promedio} por lo tanto error")

#Extension Rainbow CSV