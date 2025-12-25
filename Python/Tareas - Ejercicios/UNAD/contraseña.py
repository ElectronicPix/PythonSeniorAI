import random

# --- CLASE PADRE (Aquí aplicamos la Herencia básica) ---
class GeneradorBase:
    def __init__(self, longitud_usuario):
        self.longitud = longitud_usuario
        # Definimos los caracteres especiales que pide la guía
        self.caracteres_especiales = "$?=)(/*-+%&#!"

    # Este método existe aquí para demostrar POLIMORFISMO más adelante
    def crear_contrasena(self):
        print("Este es el generador base, aun no hace nada complejo.")

# --- CLASE HIJA (Aquí hereda de la clase de arriba) ---
class GeneradorFinal(GeneradorBase):
    def __init__(self, longitud_usuario):
        # Usamos super() para traer los datos de la clase padre
        super().__init__(longitud_usuario)

    # APLICAMOS POLIMORFISMO: Cambiamos cómo funciona el método 'crear_contrasena'
    def crear_contrasena(self):
        # Primero validamos que sea mayor a 8
        if self.longitud < 8:
            print("¡Error! La contraseña debe tener mínimo 8 caracteres.")
            return None # Salimos si no cumple

        # Listas de letras y números simples
        mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        minusculas = "abcdefghijklmnopqrstuvwxyz"
        numeros = "0123456789"

        # Paso 1: Asegurar uno de cada tipo (Obligatorio)
        # Usamos random.choice para elegir uno al azar de cada grupo
        letra_may = random.choice(mayusculas)
        letra_min = random.choice(minusculas)
        numero = random.choice(numeros)
        simbolo = random.choice(self.caracteres_especiales)

        # Guardamos estos 4 fijos en una lista
        contrasena_lista = [letra_may, letra_min, numero, simbolo]

        # Paso 2: Rellenar lo que falta
        # Juntamos todos los caracteres posibles en una sola bolsa grande
        todos_los_caracteres = mayusculas + minusculas + numeros + self.caracteres_especiales

        # Calculamos cuántos nos faltan para completar la longitud que pidió el usuario
        faltantes = self.longitud - 4

        # IMPORTANTE: Para que NO se repitan, quitamos los que ya usamos
        # Creamos una lista temporal para sacar caracteres
        bolsa_sin_repetidos = []
        for letra in todos_los_caracteres:
            if letra not in contrasena_lista:
                bolsa_sin_repetidos.append(letra)

        # Verificamos si alcanzan los caracteres (por si pide una contraseña gigante)
        if len(bolsa_sin_repetidos) < faltantes:
            print("La longitud es muy grande para no repetir caracteres.")
            return None

        # Elegimos al azar los que faltan SIN repetir (usando random.sample)
        relleno = random.sample(bolsa_sin_repetidos, faltantes)

        # Sumamos los obligatorios + el relleno
        contrasena_lista = contrasena_lista + relleno

        # Paso 3: Desordenar todo para que sea aleatorio
        random.shuffle(contrasena_lista)

        # Convertimos la lista en texto
        resultado_final = "".join(contrasena_lista)
        return resultado_final

# --- PROGRAMA PRINCIPAL ---
# Esto es lo que se ejecuta cuando le das play
print("--- TAREA 5: GENERADOR DE CONTRASEÑAS UNAD ---")
print("Estudiante de Ingeniería Electrónica")
print("----------------------------------------------")

try:
    # Pedimos el dato al usuario
    dato = input("Ingrese la longitud de la contraseña (número entero, mín 8): ")
    longitud_ingresada = int(dato) # Convertimos a entero

    # Creamos el objeto (Instancia) de la clase Hija
    mi_objeto = GeneradorFinal(longitud_ingresada)

    # Llamamos a la función para generar la clave
    password_generada = mi_objeto.crear_contrasena()

    if password_generada:
        print("\nRESULTADO:")
        print(f"Su contraseña segura es: {password_generada}")
        print("¡Proceso finalizado correctamente!")
    
except ValueError:
    # Esto cumple el requisito de "Manejo de Excepciones"
    print("\nERROR: Debes ingresar un NÚMERO válido, no letras.")

except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")