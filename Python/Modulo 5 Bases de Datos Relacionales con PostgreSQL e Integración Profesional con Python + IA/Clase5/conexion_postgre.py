import psycopg2
from psycopg2 import OperationalError, Error  # importar errores personalizados
import os
from dotenv import load_dotenv

# Cargar variables desde archivo
load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

"""Establecer conexión"""
conn = None

"""
    Errores personalizados 
"""


def conectar():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
        )
        print("\nconexion ok")
        return conn
    except OperationalError as oe:
        print(f"[Error] Problema operacional al conectar: {oe}")
    except Error as e:
        print(f"[Error] psycopg2 Error al conectar: {e}")
    except Exception as ex:
        print(f"[Error] Inesperado: {ex}")
    return None


conexion = conectar()

"""Visualizar información (Consultas)"""


def llamar_usuario(conn: psycopg2.extensions.connection):

    query = """SELECT * FROM usuario"""

    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
            filas = cursor.fetchall()  # Llama la información
            for f in filas:
                print(f)
    except Error as e:
        print(f"[Error] psycopg2 Error al conectar: {e}")


"""Insertar información"""


def insertar_usuario(conn: psycopg2.extensions.connection, nombre, email):
    query = """INSERT INTO usuario(nombre, email)
    VALUES(%s, %s)"""

    try:
        with conn.cursor() as cursor:
            cursor.execute(query, (nombre, email))
        conn.commit()
        print("[ok] Insercion segura registrada")
    except Error as e:
        conn.rollback()  # Si hay un error, para que el dato no quede en la fila
        print(f"[Error] psycopg2 Error al conectar: {e}")


conn = conectar()
insertar_usuario(conn, "Matias Perez", "matias.perez@gmail.com")
llamar_usuario(conexion)
conn.close()
