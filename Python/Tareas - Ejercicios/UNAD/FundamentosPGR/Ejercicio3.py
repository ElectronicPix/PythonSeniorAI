"""Problema 3: Una pequeña oficina de Recursos Humanos necesita automatizar el cálculo
de los salarios netos de sus empleados a partir de sus horas trabajadas y una tarifa base,
aplicando un descuento fijo. Los datos iniciales están disponibles, pero el proceso de cálculo,
validación y presentación del informe es propenso a errores manuales. Desarrollar un programa en 
Python que maneje una lista de empleados (con sus horas trabajadas y tarifa por hora), realice el 
cálculo del salario bruto y neto (aplicando un descuento del 15%), y genere un informe final."""

# Datos iniciales de los empleados
DATOS_EMPLEADOS = [
    {"nombre": "Ana García", "horas": 160, "tarifa": 15.5},
    {"nombre": "Luis Pérez", "horas": 150, "tarifa": 18.0},  # Corregido: horas como número
    {"nombre": "Marta López", "horas": 165, "tarifa": 12.0}
]

TASA_DESCUENTO = 0.15

def calcular_bruto(h, t):
    """Calcula el salario bruto."""
    return h * t

def calcular_neto(salario_bruto):
    """Calcula el salario neto aplicando el descuento."""
    descuento = salario_bruto * TASA_DESCUENTO
    return salario_bruto - descuento

def generar_informe(lista_empleados):
    for empleado in lista_empleados:
        nombre = empleado['nombre']
        horas = empleado['horas']
        tarifa = empleado['tarifa']
        salario_bruto = calcular_bruto(horas, tarifa)
        salario_neto = calcular_neto(salario_bruto)
        print(f"Informe de {nombre}: Salario Bruto: ${salario_bruto:.2f}, Salario Neto: ${salario_neto:.2f}")

generar_informe(DATOS_EMPLEADOS)