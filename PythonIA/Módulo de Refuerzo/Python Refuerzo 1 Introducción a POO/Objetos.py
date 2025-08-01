"""
    En python, todo es un objeto, y las funciones son objetos de primera clase.
"""
numero = 10 # número es un objeto de la clase int
#print(type(numero))  # <class 'int'>

#integer (int) es una clase y numero es una instancia de int
#string (str) es una clase, y cadena es una instancia de la clase str
#boolean (bool) es una clase, y verdadero es una instancia de la clase bool

#Funciones en poo se llaman métodos
#variables son atributos

cadena = "Hola mundo. Hello world" # cadena es un objeto de la clase str
#print(cadena.upper()) Llama al método upper de la clase str, que devuelve la cadena en mayúsculas
#print(cadena.isdigit()) Llama al método isdigit, que devuelve True si la cadena contiene solo dígitos
print(cadena.split())  # Llama al método split de la clase str, que divide la cadena en una lista de palabras

def mi_funcion():
    pass

print(type(mi_funcion))  # <class 'function'>, mi_funcion es un objeto de la clase function
#funtion es una clase, y mi_funcion es una instancia de la clase function

