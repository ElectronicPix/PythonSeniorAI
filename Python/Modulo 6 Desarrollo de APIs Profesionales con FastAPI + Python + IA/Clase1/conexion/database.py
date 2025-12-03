import psycopg2
from psycopg2.extras import RealDictCursor # Cambia el formato de una tupla a diccionario para facilitar la lectura  en Json

def get_connection():
    conn = psycopg2.connect(
        host = "localhost",
        database = "school",
        user = "postgres",
        password = "admin",
        port = "5432"
        cursor_factory= RealDictCursor # Para obtener diccionarios en lugar de tuplas
    )
    return conn