#Base de datos en memoria
libros = []
socios = []
auxContador = 1

def mostrar_menu():
    '''Muestra las opcines del menu.'''
    print(" MINIBIBIOTECA ")
    print("1. Registrar Libro")
    print("2. Registrar un Sucio")
    print("3. Prestar Libro")
    print("4. Devolver Libro")
    print("5. Ver libros Prestados")
    print("6. Ver todos los Libros")
    print("7. Ver todos los Socios")
    print("0. Salir") #Opción cero por modificación.

def registrar_libro():
    pass  
 
def registrar_socio():
    pass

def prestar_libro():
    pass

def devolver_libro():
    pass

def ver_libro_prestado():
    pass

def ver_todos_libros():
    pass

def ver_todos_socios():
    pass

def main():
    '''Funcion principal del programa'''
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opcion (0-7): ").strip()
        '''
        opciones de condicionales
        if opcion == '1':
            pass
        elif opcion == '2':
            pass
        '''
        
        match opcion:
            case '1':
                registrar_libro()
            case '2':
                registrar_socio()
            case '3':
                prestar_libro()
            case '4':
                devolver_libro()
            case '5':
                ver_libro_prestado()
            case '6':
                ver_todos_libros()
            case '7':
                ver_todos_socios()
            case '0':
                print("📚 Gracias por usar MiniBiblio! 📚")
                print("📚 Hasta Luego 📚")
                break
            case _:
                print("Opcion no valida. Por favor seleccione una opcion del 0 al 7")