# *******************************************************
# Nombre del estudiante: Rubén Darío De La Puente Castro
# Grupo: 1022
# Programa: Ingeniería Electrónica
# Código Fuente: autoría propia
# *******************************************************
"""Problema 3: Un nuevo operador de televisión por cable desea ofrecer nuevos servicios en su ciudad.
Para esto, se requiere saber en una muestra de 50 personas:
- Cuántas horas a la semana invierten en ver televisión.
- Qué tipo de canal prefieren ver: deportivo, cultural, de noticias o de películas.
- Cuántas personas están dispuestas a pagar más de 50 mil pesos por el servicio de televisión.
- La edad de la persona

El programa debe mostrar:
- El promedio de horas semanales que invierten los encuestados en ver televisión.
- La cantidad de personas interesadas en cada canal: deportivo, cultural, de noticias o de películas.
- La cantidad de personas que están dispuestas a pagar más de 50 mil pesos por el servicio.
- El promedio de edades de los encuestados."""

"""
total_horas = 0
total_edades = 0
pago_mayor_50k = 0
canales = [0, 0, 0, 0] # Deportivo, Cultural, Noticias, Películas

Muestra = 50

for i in range(1, Muestra + 1):
    print(f"\nEncuesta {i}/ {Muestra}:")
    total_horas = int(input("Ingrese las horas semanales que invierte en ver televisión: "))
    total_edades = int(input("Ingrese su edad: "))
    pago_mayor_50k = float(input("¿Está dispuesto a pagar más de 50 mil pesos por el servicio de televisión? (1: sí/ 0: no): "))
    if pago_mayor_50k == 1:
        pago_mayor_50k += 1 
    
    canal = input   ("¿Qué tipo de canal prefiere ver? (deportivo, cultural, noticias, películas): ").strip().lower()
    if canal == 'deportivo':
        canales[0] += 1 
    elif canal == 'cultural':
        canales[1] += 1 
    elif canal == 'noticias':
        canales[2] += 1     
    elif canal == 'peliculas':
        canales[3] += 1
        
promedio_horas = total_horas / Muestra
promedio_edades = total_edades / Muestra        
print(f"\nResultados de la encuesta:")
print(f"Promedio de horas semanales que invierten en ver televisión: {promedio_horas:.2f} horas")
print(f"Cantidad de personas interesadas en cada canal:")
print(f"Deportivo: {canales[0]}")       
print(f"Cultural: {canales[1]}")
print(f"Noticias: {canales[2]}")
print(f"Películas: {canales[3]}")
print(f"Cantidad de personas dispuestas a pagar más de 50 mil pesos por el servicio: {pago_mayor_50k}")
print(f"Promedio de edades de los encuestados: {promedio_edades:.2f} años")

"""

total_horas = 0
total_edades = 0
pago_alto = 0
canales = [0, 0, 0, 0] # Deportivo, Cultural, Noticias, Películas

MUESTRA = 4

for i in range(1, MUESTRA + 1):
    print(f"\nEncuesta {i}/{MUESTRA}")
    total_horas += float(input("Horas de TV semanales: "))
    total_edades += int(input("Edad: "))
    pago = float(input("¿Cuánto pagaría?: "))
    if pago > 50000: pago_alto += 1
    
    op = int(input("Canal (1:Dep, 2:Cult, 3:Not, 4:Pel): "))
    if 1 <= op <= 4: canales[op-1] += 1

print(f"\nPromedio Horas: {total_horas/MUESTRA:.2f}")
print(f"Promedio Edades: {total_edades/MUESTRA:.2f}")
print(f"Interesados pago > 50k: {pago_alto}")
print(f"Canales: Dep:{canales[0]}, Cult:{canales[1]}, Not:{canales[2]}, Pel:{canales[3]}")