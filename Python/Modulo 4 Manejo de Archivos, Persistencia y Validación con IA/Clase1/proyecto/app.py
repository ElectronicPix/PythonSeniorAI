tareas = ("Tarea 1: Estudiar Python",
        "Tarea 2: Hacer ejercicios") #Tupla

archivo = open("tareas3.txt","w")

for tarea in tareas:
    archivo.write(tarea)
    archivo.write("\n")

archivo.close()

#Lectura

'''
"r" Lectura
"w" Escritura
"a" Agregar
"r+" Lectura y escritura
'''


with open("tareas.txt") as archivo:
    lineas = archivo.readlines()
    print(lineas)

nueva_tarea = "Tarea 3: Ir al parque"
with open("tareas.txt", "a") as archivo:
    archivo.write("\n")
    archivo.write(nueva_tarea)
    
with open("tareas.txt", "w") as archivo:
    pass