from prettytable import PrettyTable

#Base de datos en memoria
libros = [
    {
    'isbn': '1',
    'titulo': 'The C++ Programming Language',
    'autor': 'Bjarne Stroustrup',
    'estado': 'Disponible',
    'socio_prestado': None
}, 
{
    'isbn': '2',
    'titulo': 'Clean Code: A Handbook of Agile Software Craftsmanship',
    'autor': 'Robert C. Martin',
    'estado': 'Disponible',
    'socio_prestado': None
}, 
{
    'isbn': '3',
    'titulo': 'Design Patterns: Elements of Reusable Object-Oriented Software',
    'autor': 'Erich Gamma',
    'estado': 'Disponible',
    'socio_prestado': None
}, 
{
    'isbn': '4',
    'titulo': 'You Don\'t Know JS: Up & Going',
    'autor': 'Kyle Simpson',
    'estado': 'Disponible',
    'socio_prestado': None
}
]
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
    global libros
    
    print("=======================================")
    print("Registrar Libros 📘")
    print("Digite 0 si quiere cancelar la creación")
    print("=======================================")
    
    titulo = input("Titulo del Libro: ").strip().lower()
    
    if titulo == '0': return #sale de la función en caso de presionar el cero
    
    if not titulo:
        print("❌ El titulo no puede estar vacio ❌")
        #return
        registrar_libro()
    
    autor = input("Autor del Libro: ").strip().lower()
    
    if autor == '0': return #sale de la función en caso de presionar el cero
    
    if not autor:
        print("❌ El Autor no puede estar vacio ❌")
        #return
        registrar_libro()
    
    isbn = input("ISBN del Libro: ").strip().lower()
    
    if isbn == '0': return #sale de la función en caso de presionar el cero
    
    if not isbn:
        print("❌ El isbn no puede estar vacio ❌")
        #return
        registrar_libro()
    
    for l in libros: # Verificamos que el libro no este agregado.
        if l['isbn'] == isbn:
            print(f"❌ Ya existe un libro con el ISBN {isbn} ❌")
            
    #Crear nuevo Libro
    nuevo_libro = { # Variable nuevo_libro almace la información que luego se agrega a la lista libro
        'isbn': isbn,
        'titulo': titulo, 
        'autor': autor, 
        'estado': 'Disponible', 
        'socio_prestado': None
    }
    
    libros.append(nuevo_libro)
    print("✔ Libro Registrado Exitosamente 📘")
    print(f"📚 {titulo} - {autor}")
    print(f"ISBN: {isbn}")
    
    print("==============================================")
 
def registrar_socio():
    pass

def prestar_libro():
    pass

def devolver_libro():
    pass

def ver_libro_prestado():
    pass

def ver_todos_libros():
    table = PrettyTable()
    table.field_names = ["Titulo", "Autor", "isbn", "estado"] # Encabezado de la tabla
    table.title = "📚 Mostrando todos los libros 📚"
    for i, libro in enumerate(libros, 1):
        table.add_row([libro["titulo"], libro["autor"], libro["isbn"], libro["estado"]])
    print(table)  
        
    '''
    print("=============================")
    print("Mostrando todos los libros")
    print("=============================")
    
    if not libros:
        print("No hay libros registrados en la biblioteca")
        return
    
    for i, libro in enumerate(libros, 1):
        print("=========================================")
        print(f"{i}. Nombre del libro: {libro["titulo"]}")
        print(f"     Autor: {libro["autor"]}")
        print(f"     ISBN: {libro["isbn"]}")
        print(f"     Estado: {libro["estado"]}")
        print("")
        '''

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
                
                
                
main()               
#Texto Lorem Ipsum: Texto de prueba