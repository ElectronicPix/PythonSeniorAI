# Definimos una lista llamada 'estudiantes'
estudiantes = [
    {
        "nombre": "Ana Torres",
        "edad": 21,
        "curso": "Ingeniería Electrónica",
        "semestre": 5
    },
    {
        "nombre": "Luis Rojas",
        "edad": 23,
        "curso": "Ingeniería de Software",
        "semestre": 7
    },
    {
        "nombre": "Sofía Castro",
        "edad": 20,
        "curso": "Ciencia de Datos",
        "semestre": 4
    }
]

'''Acceder a un estudiante completo (un diccionario):
Para ver la información del primer estudiante (índice 0).'''
# Imprime el primer diccionario de la lista
print(estudiantes[0])
# Salida: {'nombre': 'Ana Torres', 'edad': 21, 'curso': 'Ingeniería Electrónica', 'semestre': 5}


'''Acceder a un dato específico de un estudiante:
Para obtener el nombre del segundo estudiante (índice 1).'''
# Primero accede al diccionario en el índice 1, luego a la clave "nombre"
nombre_segundo_estudiante = estudiantes[1]["nombre"]
print(nombre_segundo_estudiante)
# Salida: Luis Rojas

'''Recorrer la lista para mostrar la información:
Puedes usar un bucle for para iterar sobre cada diccionario en la lista y mostrar los datos 
de forma ordenada.
'''

print("\n--- Reporte de Estudiantes ---")
for estudiante in estudiantes:
  print(f"Nombre: {estudiante['nombre']}, Curso: {estudiante['curso']}")

# Salida:
# --- Reporte de Estudiantes ---
# Nombre: Ana Torres, Curso: Ingeniería Electrónica
# Nombre: Luis Rojas, Curso: Ingeniería de Software
# Nombre: Sofía Castro, Curso: Ciencia de Datos
