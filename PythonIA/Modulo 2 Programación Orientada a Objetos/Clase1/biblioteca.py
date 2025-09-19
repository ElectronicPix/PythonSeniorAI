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
    print("2. Registrar un Socio")
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
    global socios, auxContador
    
    print("=======================================")
    print("Registrar Socio 👤")
    print("Digite 0 si quiere cancelar la creación")
    print("=======================================")
    
    nombre = input ("Nombre del socio: ").strip().lower()
    
    if nombre == "0": return
    
    if not nombre: 
        print("❌El nombre no puede estar vacio ❌")
        return
    
    apellido = input("Apellido del socio: ").strip().lower()
    
    if apellido == "0": return
    
    if not apellido: 
        print("❌El apellido no puede estar vacio ❌")
        return
    
    email = input("Email del socio: ").strip().lower()
    
    if email == "0": return
    
    if not email: 
        print("❌El email no puede estar vacio ❌")
        return
    
    for socio in socios: # Verificamos que el libro no este agregado.
        if socio['email'] == email:
            print(f"❌ Ya existe un libro con el ISBN {email} ❌")
    
    #Crear nuevo socio
    nuevo_socio = { # Variable nuevo_libro almace la información que luego se agrega a la lista libro
        'id': f'{auxContador}', #f'Socio-{auxContador:03d}'
        'nombre': nombre, 
        'apellido': apellido, 
        'email': email, 
        'libros_prestados': [] # para almacenar los libros prestados.
    }
    
    socios.append(nuevo_socio)
    auxContador += 1 #Incrementa el id del socio cada que se ingresa uno nuevo
    print("✔ Socio Registrado Exitosamente 👤")
    print(f"👤 {nombre}  {apellido}")
    print(f"📧 email: {email}")
    print(f"ID: {nuevo_socio['id']}")
    
    print("==============================================")

def prestar_libro():
    '''Prestar un libro a un socio'''
    global libros, socios
    
    print("📚 Prestamo de libros 📚")
    
    '''Pedir ISBN del libro'''
    isbn = input("ISBN del libro a prestar: ").strip()
    
    if not isbn:
        print("❌ El ISBN no puede estar vacio ❌")
        return
    
    '''Buscar un libro'''
    libro_encontrado = None
    
    for libro in libros:
        if libro['isbn'] == isbn:
            libro_encontrado = libro
            break
        
    if not libro_encontrado:
        print(f"No se encontro un libro con el ISBN {isbn}")
        return
    
    '''Pedir ID del socio'''
    id_socio = input("ID del socio: ").strip().lower()
    
    if not id_socio:
        print("❌ El id no puede estar vacio ❌")
        return
    
    '''Buscar un socio'''
    id_socio_encontrado = None
    
    for socio in socios:
        if socio['id'] == id_socio:
            id_socio_encontrado = socio
            break
        
    if not id_socio_encontrado:
        print(f"No se encontro un usuario con el id {id_socio}")
        return
    #Verificar que el libro este disponible
    disponible_libro = None
    for libro in libros:
        if libro['estado'] == 'Disponible':
            disponible_libro = True
            break
            
    if not disponible_libro:
        print("Actualmente el libro solicitado no está disponible")
        return
    
    libro_encontrado['estado'] = 'Prestado' 
    libro_encontrado['socio_prestado'] = id_socio
    
    print("\n")
    print("Libro prestado con exito 📘")
    print(f"Libro: {libro_encontrado['titulo']}")
    print(f"Prestado a: {id_socio_encontrado['nombre']}")
    

def devolver_libro():
    global libros
    
    '''Pedir ISBN del libro'''
    isbn = input("ISBN del libro a prestar: ").strip()
    
    if not isbn:
        print("❌ El ISBN no puede estar vacio ❌")
        return
    
    '''Buscar un libro'''
    libro_encontrado = None
    
    for libro in libros:
        if libro['isbn'] == isbn:
            libro_encontrado = libro
            break
        
    if not libro_encontrado:
        print(f"No se encontro un libro con el ISBN {isbn}")
        return
    
    
    libro_encontrado['estado'] = 'Disponible'
    libro_encontrado['socio_prestado'] = None
    
    print("Libro devuelto exitosamente")

def ver_libro_prestado():
    #Opción que muestre que no hay libros prestados, que los socios salga que tiene un libro prestado.
    table = PrettyTable()
    table.field_names = ["Titulo", "Autor", "isbn", "id_socio"] # Encabezado de la tabla
    table.title = "📚 Mostrando todos los libros prestados 📚"
    
    if not libros:#Pendiente modificac
        print("==========================================")
        print("No hay libros prestados en la biblioteca")
        print("===========================================")
        return
    
    for i, libro in enumerate(libros, 1):
        if libro['estado'] == 'Prestado':
            table.add_row([libro["titulo"], libro["autor"], libro["isbn"], libro["socio_prestado"]])
    print(table) 
    

def ver_todos_libros():
    table = PrettyTable()
    table.field_names = ["Titulo", "Autor", "isbn", "estado"] # Encabezado de la tabla
    table.title = "📚 Mostrando todos los libros 📚"
    
    if not libros:
        print("==========================================")
        print("No hay libros registrados en la biblioteca")
        print("===========================================")
        return
    
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
    table = PrettyTable()
    table.field_names = ["ID", "Nombre", "Apellido", "Email", "Libros Prestados"] # Encabezado de la tabla
    table.title = "👤 Mostrando todos los socios 👤"
    
    if not socios:
        print("==========================================")
        print("No hay socios registrados en la biblioteca")
        print("===========================================")
        return
    
    for socio in socios:
        libros_prestados = len(socio["libros_prestados"]) #verifica si hay libros prestados usando el len
        table.add_row([socio["id"], socio["nombre"], socio["apellido"], socio["email"], libros_prestados])
    print(table) 

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
                registrar_libro() # Hecho
            case '2':
                registrar_socio()#Hecho
            case '3':
                prestar_libro()#Hecho
            case '4':
                devolver_libro()
            case '5':
                ver_libro_prestado()
            case '6':
                ver_todos_libros()#Hecho
            case '7':
                ver_todos_socios()#Hecho
            case '0':
                print("📚 Gracias por usar MiniBiblio! 📚")
                print("📚 Hasta Luego 📚")
                break
            case _:
                print("Opcion no valida. Por favor seleccione una opcion del 0 al 7")
                
                
                
main()               
#Texto Lorem Ipsum: Texto de prueba