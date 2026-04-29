# *******************************************************
# Nombre del estudiante: Rubén Darío De La Puente Castro
# Grupo: 1022
# Programa: Ingeniería Electrónica
# Código Fuente: autoría propia
# *******************************************************
"""Problema 2: En un conjunto residencial, cada vecino debe pagar una cuota mensual para el mantenimiento. El administrador quiere
un programa que revise uno por uno a todos los vecinos para lo cual el usuario debe ingresar la cantidad de residentes de la unidad
residencial y el valor de la cuota mensual.

Por cada vecino, el sistema debe pedir si ya pagó su cuota o no. Si el vecino pagó, se registra como “al día”; si no pagó, el programa
lo registra como “moroso”.

Este proceso debe repetirse hasta haber revisado a todos los vecinos.

Al finalizar, el programa muestra cuántas personas están al día y cuántas están atrasadas y cuanto es el valor total adeudado por los vecinos
morosos."""


print("--- Gestión de Pasgos - Conjunto Residencial ---")
cantidad_vecinos = int(input("Ingrese la cantidad de vecinos en la unidad residencial: "))
valor_cuota = float(input("Ingrese el valor de la cuota mensual: "))

al_dia = 0
morosos = 0
deuda_totasl = 0.0

for i in range(1, cantidad_vecinos + 1):
    print(f"\nVecino {i}:")
    pago= input("¿El vecino ha pagado su cuota? (1: sí/ 0: no): ").strip().lower()
    if pago == '1':
        al_dia += 1
    else:
        morosos += 1
        deuda_totasl += valor_cuota

print(f"\nResumen:")
print(f"Vecinos al día: {al_dia}")
print(f"Vecinos morosos: {morosos}")
print(f"Deuda total: ${deuda_totasl:.2f}")