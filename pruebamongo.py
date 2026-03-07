from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["Alumnos"]


# Crear una colección
col = db["DatosBasicos"]

"""
# Crear un documento
documento = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

# Agregar el documento a la colección
col.insert_one(documento)

"""

# 3. Preparar la lista de documentos
documentos = [
    {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"},
    {"nombre": "Maria", "edad": 25, "ciudad": "Barcelona"},
    {"nombre": "Carlos", "edad": 35, "ciudad": "Valencia"},
    {"nombre": "Ana", "edad": 28, "ciudad": "Sevilla"},
]

# 4. Insertar múltiples datos
resultado = col.insert_many(documentos)

# 5. Confirmación
print(f"Se insertaron {len(resultado.inserted_ids)} documentos con éxito.")
print(f"IDs generados: {resultado.inserted_ids}")


"""Obtener UN solo documento (find_one)"""

# Buscar el primer documento que coincida con el nombre "Juan"
documento = col.find_one({"nombre": "Juan"})

if documento:
    print("Datos encontrados:")
    print(f"Nombre: {documento['nombre']}, Edad: {documento['edad']}")
else:
    print("No se encontró ningún documento.")


"""Obtener VARIOS documentos (find)"""

# Buscar todos los que vivan en "Madrid"
resultados = col.find({"ciudad": "Madrid"})

print("Personas en Madrid:")
for doc in resultados:
    print(f"- {doc['nombre']} ({doc['edad']} años)")


"""Obtener TODO el contenido de la colección"""

todos_los_datos = col.find()

for registro in todos_los_datos:
    print(registro)
