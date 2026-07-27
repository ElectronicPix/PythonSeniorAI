"""print("hola mundo")
# Crear una variable
nombre = "Juan"
edad = 25
altura = 1.75
es_estudiante = True

# Mostrar las variables
print(nombre)
print(edad)
print(altura)
print(es_estudiante)

# ✅ Nombres válidos
mi_variable = "Válido"
variable123 = "Válido"
MiVariable = "Válido"
_variable = "Válido"

# ❌ Nombres NO válidos
# 123variable = "Error"  # No puede comenzar con número
# mi-variable = "Error"  # No puede usar guiones
# if = "Error"  # No puede usar palabra reservada

nombre_apellido = "Juan Pérez"  # Válido, usa guion bajo
print(nombre_apellido)  # Esto causará un error de sintaxis

print(type(nombre))
print(type(edad))
print(type(altura))
print(type(es_estudiante))

# Strings con comillas simples
nombre = 'Juan David'
ciudad = 'Bogotá'

# Strings con comillas dobles
mensaje = "¡Hola mundo!"
frase = "Python es genial"

# Strings multilínea
texto_largo = Este es un texto
que puede ocupar
múltiples líneas
sin necesidad de usar caracteres especiales, gracias a las comillas triples.

print(nombre)
print(texto_largo)
"""

nombre = int(input("Ingrese su edad:  "))

print(f"La suma de la edad de {nombre} más 10 años es: {nombre + 10}")

# Ejemplos de operadores aritméticos
a = 10
b = 3
print("Suma:", a + b)  # 13
print("Resta:", a - b)  # 7
print("Multiplicación:", a * b)  # 30
print("División:", a / b)  # 3.333...
print("División entera:", a // b)  # 3
print("Módulo:", a % b)  # 1
print("Potencia:", a ** b)  # 1000

# Ejemplos de operadores de comparación
edad = 18
altura = 1.75
print("¿Es mayor de edad?", edad >= 18)  # True
print("¿Es alto?", altura > 1.80)  # False
print("¿Es exactamente 18?", edad == 18)  # True
print("¿No es 20?", edad != 20)  # True

# Ejemplos de operadores lógicos
es_estudiante = True
es_mayor_de_edad = True
tiene_experiencia = False

# AND: ambas condiciones deben ser True
puede_trabajar = es_estudiante and es_mayor_de_edad
print("¿Puede trabajar?", puede_trabajar)  # True

# OR: al menos una condición debe ser True
es_calificado = es_estudiante or tiene_experiencia
print("¿Está calificado?", es_calificado)  # True

# NOT: invierte el valor
no_es_estudiante = not es_estudiante
print("¿No es estudiante?", no_es_estudiante)  # False
