
"""Problema 1: La empresa de energía “LowCost” necesita un sistema que permita 
clasificar el consumo mensual en kWh y aplicar los ajustes correspondientes en la facturación.
El programa debe:
1)Solicitar al usuario el consumo mensual en kWh.
2)Clasificar el consumo en:
-Bajo: menos de 150 kWh.
-Medio: entre 150 kWh y 350 kWh.
-Alto: más de 350 kWh.
3)Calcular el valor base del consumo usando el costo por kWh:
Costo por kWh=320,5 COP
4)Aplicar los ajustes:
a.Consumo bajo: descuento del 5%.
b.Consumo medio: sin ajuste.
c.Consumo alto: recargo del 12%.
Salida esperada:
-Categoría del consumo.
-Valor base.
-Porcentaje de descuento o recargo aplicado.
-Valor final a pagar."""

print("|---------------------------------------|")
print("|-----Emepresa Energía LowCost 📈-------|")
print("|---------------------------------------|\n")

costo_kwh = 320.5

Consumo_Mensual_kwh = float(input("Ingrese el consumo mensual en KWh: "))

if Consumo_Mensual_kwh < 150:
    categoria = "bajo consumo"
    porcentaje_ajuste = - 5
elif 150 <= Consumo_Mensual_kwh <=350:
    categoria = "Medio"
    porcentaje_ajuste = 0
else: 
    categoria = "Alto consumo"
    porcentaje_ajuste = 12
    
valor_base = Consumo_Mensual_kwh * costo_kwh

ajuste_calculado = valor_base * (porcentaje_ajuste / 100)

valor_final = valor_base + ajuste_calculado

# Salida esperada
print("\n"+"="*30)
print(" RESUMEN DE FACTURACIÓN")
print("="*30)
print(f"Categoría del consumo: {categoria}")
print(f"Valor base: {valor_base:,.2f} COP")
print(f"Ajuste aplicado: {porcentaje_ajuste} %")
print(f"Valor final a pagar: {valor_final:,.2f} COP")