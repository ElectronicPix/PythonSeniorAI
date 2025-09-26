import mysql.connector

# https://spark.apache.org/

# Conexión a la base de datos
conexion = mysql.connector.connect(  # puntos de acceso
    host="localhost",  # 127.1.1 es localhost, no olvidar la coma
    user="root",
    password="root",
    database="tienda",  # base de datos
    port=3306,  # Puerto de conexión
)

cursor = conexion.cursor() # pin de conexión, permite hacer consulta

def leer_datos():
    #cursor.execute("select * from clientes where nombre like 'j%';")
    cursor.execute("select * from clientes;")

    resultado = cursor.fetchall() # Guarda cuando se recupera información (tablas y demás)

    #print(type(resultado))

    for fila in resultado:
        print(fila)
   
def crear_clientes(nombre,correo,edad):
    cursor.execute(f"INSERT INTO clientes(nombre, correo, edad) values('{nombre}', '{correo}', {edad});")
    conexion.commit()
    print("Cliente creado")
    

crear_clientes("Luz", "luz@gmail.com", 30)

# Recomendable cerrar los procesos
conexion.close()
cursor.close()

