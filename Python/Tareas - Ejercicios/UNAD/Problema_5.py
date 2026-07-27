# ==========================================
# Fase 5 - Evaluación Final POA
# Solución al Problema 1: Nivel de compromiso
# ==========================================
# Este programa clasifica el nivel de compromiso de usuarios
# basándose en la duración de la sesión y el número de clics realizados.
# ==========================================

def clasificar_compromiso(duracion, clics):
    """
    Módulo para calcular la clasificación de compromiso de una sesión 
    basándose en su duración y clics.
    
    Parámetros:
        duracion (int): Duración de la sesión en segundos
        clics (int): Número de eventos de clics realizados
    
    Retorna:
        str: Clasificación del compromiso ("Alto", "Medio" o "Bajo")
    """
    # Verificar si el compromiso es "Alto"
    # Condición: Duración mayor a 180 segundos (3 minutos) AND Clics mayor a 8
    if duracion > 180 and clics > 8:
        return "Alto"
    
    # Verificar si el compromiso es "Bajo"
    # Condición: Duración menor a 60 segundos (1 minuto) OR Clics menor a 3
    elif duracion < 60 or clics < 3:
        return "Bajo"
    
    # Si no cumple ninguna de las condiciones anteriores, clasificar como "Medio"
    # Esto ocurre cuando: (duracion >= 60 y duracion <= 180) o (clics >= 3 y clics <= 8)
    else:
        return "Medio"

def main():
    """
    Función principal que ejecuta el programa.
    Procesa una matriz de datos de sesiones y genera un informe de clasificación.
    """
    # ===== DATOS INICIALES =====
    # Crear una matriz con datos de sesiones de usuarios
    # Formato de cada fila: [ID Cliente, Duración (segundos), Eventos Clics]
    # Incluye al menos 5 filas de datos para analizar
    matriz_sesiones = [
        # Sesión 1: ID 1001, Duración 200s, 10 clics -> Cumple para Alto (200 > 180 y 10 > 8)
        [1001, 200, 10],
        # Sesión 2: ID 1002, Duración 45s, 5 clics -> Cumple para Bajo (45 < 60)
        [1002, 45, 5],
        # Sesión 3: ID 1003, Duración 150s, 6 clics -> Cumple para Medio (no cumple Alto ni Bajo)
        [1003, 150, 6],
        # Sesión 4: ID 1004, Duración 190s, 2 clics -> Cumple para Bajo (2 < 3, a pesar de duración)
        [1004, 190, 2],
        # Sesión 5: ID 1005, Duración 210s, 8 clics -> Cumple para Medio (clics no es > 8, es exactamente 8)
        [1005, 210, 8],
        # Sesión 6: ID 1006, Duración 30s, 1 clic -> Cumple para Bajo (ambas condiciones menores)
        [1006, 30, 1]
    ]
    
    # ===== ENCABEZADO DEL INFORME =====
    # Imprimir una línea separadora para mejorar la presentación
    print("-" * 40)
    # Imprimir el título del informe
    print("INFORME DE COMPROMISO DE SESIONES")
    # Imprimir otra línea separadora
    print("-" * 40)
    # Imprimir los encabezados de las columnas (ID Cliente y Clasificación Final)
    print(f"{'ID Cliente':<15} | {'Clasificación Final'}")
    # Imprimir una línea separadora entre encabezados y datos
    print("-" * 40)
    
    # ===== PROCESAMIENTO DE DATOS =====
    # Recorrer cada sesión en la matriz de sesiones
    for sesion in matriz_sesiones:
        # Extraer el ID del cliente (primer elemento de la sesión)
        id_cliente = sesion[0]
        # Extraer la duración de la sesión en segundos (segundo elemento)
        duracion = sesion[1]
        # Extraer el número de clics (tercer elemento)
        clics = sesion[2]
        
        # Llamar a la función clasificar_compromiso() pasando duracion y clics
        # Esta función retorna una cadena de texto con la clasificación
        clasificacion = clasificar_compromiso(duracion, clics)
        
        # ===== SALIDA DE DATOS =====
        # Imprimir el resultado formateado: ID del cliente y su clasificación
        # Se usa formato f-string con alineación a la izquierda para mejor legibilidad
        print(f"{id_cliente:<15} | {clasificacion}")

# ===== PUNTO DE ENTRADA DEL PROGRAMA =====
# Verificar si este archivo se está ejecutando directamente (no como módulo importado)
# __name__ es "__main__" solo cuando el archivo se ejecuta directamente
if __name__ == "__main__":
    # Llamar a la función principal para iniciar el programa
    main()