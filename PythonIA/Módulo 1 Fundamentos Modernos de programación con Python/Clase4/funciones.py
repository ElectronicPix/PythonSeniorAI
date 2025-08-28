def saludar(): #funcion basica
    print("Hola estudiantes de dev senior en el curso Developer Python Senior AI")
    
#permite empaquetar un proceso    
saludar()

#fuciones con parametros
def saludarEstudiante(nombre):
    #parametro recibe literal de informacion
    print(f"Hola {nombre} bienvenido a Dev Senior")
    
saludarEstudiante("Ruben") #Argumentos o literal de informacion ("Ruben")


#funcion con retorno de valores
def  sumar(num1, num2):
    return num1 + num2

resultado = sumar(10, 8)
print(f"la suma es: {resultado}")

