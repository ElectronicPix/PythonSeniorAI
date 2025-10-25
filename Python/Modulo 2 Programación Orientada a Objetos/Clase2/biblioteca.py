from prettytable import PrettyTable

class Libro:
    
    def __init__(self, isbn, titulo, autor):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.estado = "Disponible"
        self.socio_prestado = None
    
    def prestado(self, id_socio):
        if self.estado == "Disponible":
            self.estado = "Prestado"
            self.socio_prestado = id_socio
            return True
        else:
            return False
        
    def devolver(self):
        self.estado = "Disponible"
        self.socio_prestado = None
        

class Socio:
    
    def __init__(self, id, nombre, apellido, email):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.libros_prestados = []

class Biblioteca:
    
    def __init__(self):
        self.libros = [] # lista de libro(objeto)
        self.socios = [] # lista de socio(objeto)
        self.contador_socios = 1
        self.menu()
    
    def registrar_libro(self):
        print("=======================================")
        print("Registrar Libros 📘")
        print("Digite 0 si quiere cancelar la creación")
        print("=======================================")
        
        titulo = input("Titulo del Libro: ").strip().lower()
    
        if titulo == '0': return #sale de la función en caso de presionar el cero
    
        if not titulo:
            print("❌ El titulo no puede estar vacio ❌")
            return
    
        autor = input("Autor del Libro: ").strip().lower()
    
        if autor == '0': return #sale de la función en caso de presionar el cero
    
        if not autor:
            print("❌ El Autor no puede estar vacio ❌")
            return
    
        isbn = input("ISBN del Libro: ").strip().lower()
    
        if isbn == '0': return #sale de la función en caso de presionar el cero
    
        if not isbn:
            print("❌ El isbn no puede estar vacio ❌")
            return
        
    
        for l in self.libros: # Verificamos que el libro no este agregado.
            if l.isbn == isbn:
                print(f"❌ Ya existe un libro con el ISBN {isbn} ❌")
                
        #Crear nuevo Libro
        
    
        self.libros.append(Libro(isbn, titulo, autor))
        print("✔ Libro Registrado Exitosamente 📘")
        print(f"📚 {titulo} - {autor}")
        print(f"ISBN: {isbn}")
    
        print("==============================================")
        
    
    def ver_todos_libros(self):
        
        table = PrettyTable()
        table.field_names = ["Titulo", "Autor", "isbn", "estado"] # Encabezado de la tabla
        table.title = "📚 Mostrando todos los libros 📚"
    
        if not self.libros:
            print("==========================================")
            print("No hay libros registrados en la biblioteca")
            print("===========================================")
            return
    
        for libro in self.libros:
            table.add_row([libro.titulo, libro.autor, libro.isbn, libro.estado])
        print(table)
        
        
        
    def menu(self):
        
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
        
        '''Funcion principal del programa'''
        while True:
            
            opcion = input("Selecciona una opcion (0-7): ").strip()
        
            match opcion:
                case '1': self.registrar_libro() 
                case '2': pass
                case '3': pass
                case '4': pass
                case '5': pass
                case '6': self.ver_todos_libros()
                case '7': pass
                case '0':
                    print("📚 Gracias por usar MiniBiblio! 📚")
                    print("📚 Hasta Luego 📚")
                    break
                case _:
                    print("Opcion no valida. Por favor seleccione una opcion del 0 al 7")
                
bibioteca1 = Biblioteca()