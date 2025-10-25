'''
archivo = open("tareas.txt", "w")
archivo.write("Tarea 1: Estudiar Python")
archivo.close()
'''


'''
archivo = open("tarea1.txt", "w", encoding="utf-8")# codificado en utf-8
archivo.write("Tarea 2: Estudiar pytho ñ 🧡")
archivo.close()'''


tareas = ["Tarea 1: Estudiar Python",
          "Tarea 2: Hacer Ejercicios"]

archivo = open("tareas3.txt", "w")
for tarea in tareas:
    archivo.write(tarea)
    archivo.write("\n")
archivo.close()



#lectura
with open("tareas.txt") as archivo:
    lineas = archivo.readlines()
    print(lineas)

#Agregar tarea
nueva_tarea = "Taras 2: Hacer Ejerciicios"
with open("tareas.txt", "a") as archivo:
    archivo.write("\n")
    archivo.write(nueva_tarea)
    
#borrar 
with open("tareas.txt", "w") as archivo:
    pass
    
    
    
'''
"r" lectura
"w" Escritura
"a" Agregar
"r+" Lectura y escritura
'''