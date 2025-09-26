# 1. Módulos de la librería estándar de Python
import os
import datetime

# Se deja una línea en blanco para separar los grupos
# 2. Módulos de terceros (instalados con pip)
# import requests

# Se deja una línea en blanco para separar los grupos
# 3. Tus propios módulos locales (archivos .py del mismo proyecto)
# from mi_proyecto import utils

# mi_modulo_de_ejemplo_pep8.py

# --- 1. Constantes y Nomenclatura ---

# Regla: Dejar espacios antes y después de los operadores (=).
MI_CONSTANTE_PI = 3.14159
VELOCIDAD_DE_LA_LUZ = 299792458


# --- 2. Funciones y Clases ---


# Regla: No usar espacios alrededor del signo = al definir argumentos
# con valores por defecto. Se escribe `formato="pdf"`, no `formato = "pdf"`.
def crear_reporte(datos, formato="pdf", es_urgente=False):
    """
    Esta función demuestra el uso correcto de espacios en los argumentos.
    """
    print(f"Generando reporte con formato {formato}...")

    # Regla: Espacio alrededor de operadores lógicos (if) y de comparación (==).
    if es_urgente == True:
        print("El reporte es URGENTE.")
    return True


class CalculadoraGeometrica:
    """
    Una clase de ejemplo para demostrar las convenciones de estilo.
    """

    def __init__(self, radio):
        self._radio_privado = radio

    def calcular_area_circulo(self):
        """
        Calcula el área. La fórmula usa espacios alrededor de los operadores (*, **).
        """
        # Regla: No poner espacios después de un paréntesis de apertura
        # o antes de uno de cierre: (self._radio_privado ** 2)
        area_del_circulo = MI_CONSTANTE_PI * (self._radio_privado**2)
        return area_del_circulo


# --- 3. Longitud de Línea (límite de 79 caracteres) ---

# Para evitar superar el límite de 79 caracteres, la siguiente cadena de texto
# se divide en varias líneas envolviéndola entre paréntesis, que es la
# forma preferida en Python.
mensaje_largo_bienvenida = (
    "Este es un mensaje de bienvenida para el usuario que es "
    "intencionalmente largo para demostrar cómo se deben formatear "
    "las líneas que superan el límite recomendado."
)

# --- 4. Ejecución del Código ---
if __name__ == "__main__":

    # Llamada a la función usando un argumento por palabra clave (con espacios)
    crear_reporte(["dato1", "dato2"], es_urgente=True)

    print("-" * 20)  # Separador visual

    mi_calculadora = CalculadoraGeometrica(radio=10)
    resultado_area = mi_calculadora.calcular_area_circulo()

    print(f"El área del círculo con radio 10 es: {resultado_area}")

    print("-" * 20)
    print(mensaje_largo_bienvenida)


# -*- coding: utf-8 -*-

"""
Este es un docstring para el módulo.
Describe el propósito del archivo: demostrar las buenas prácticas de PEP8.
"""

# Se dejan dos líneas en blanco para separar funciones de alto nivel o clases.


def calcular_area(radio):
    """Calcula el área de un círculo."""
    pi = 3.14159
    return pi * (radio**2)


# Se dejan dos líneas en blanco antes de la definición de una clase.


class Mascota:
    """
    Esta clase representa a una mascota.

    Atributos:
        nombre (str): El nombre de la mascota.
    """

    def __init__(self, nombre):
        # 1. Indentación: Este bloque tiene 4 espacios.
        self.nombre = nombre

    # Se deja una línea en blanco para separar métodos dentro de una clase.

    def saludar(self):
        """La mascota emite un saludo."""
        # 3. Comentarios: Debe ser conciso y tener un espacio después del #.
        mensaje = f"Hola, mi nombre es {self.nombre}"
        print(mensaje)


# --- Bloque principal de ejecución ---
# Es una buena práctica separar el código ejecutable.

mi_perro = Mascota("Fido")
mi_perro.saludar()

area_circulo = calcular_area(10)
print(f"El área del círculo es: {area_circulo}")
