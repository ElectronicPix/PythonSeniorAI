import psycopg2
from psycopg2 import OperationalError, Error  # importar errores personalizados

# Variables necesarias para el proyecto
DB_NAME = "biblioteca"  # Nombre de nuestra base de datos
DB_USER = "postgres"  # Nombre de usuario
DB_PASSWORD = "admin"  # Password de su base de datos
DB_HOST = "localhost"  # 127.0.0.1
DB_PORT = 5432  # Puerto de conexión


"""Establecer conexión"""
conn = None

"""
    Errores personalizados 
"""
try:
    conn = psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
    )
    print("\nconexion ok")
except OperationalError as oe:
    print(f"[Error] Problema operacional al conectar: {oe}")
except Error as e:
    print(f"[Error] psycopg2 Error al conectar: {e}")
except Exception as ex:
    print(f"[Error] Inesperado: {ex}")
finally:  # Cierre de la puerta de conexión
    if conn is not None:
        try:
            conn.close()
            print("conexión cerrada")
        except Exception as ex_close:
            print(f"[WARN] No se pudo cerrar limpiamente: {ex_close}")
