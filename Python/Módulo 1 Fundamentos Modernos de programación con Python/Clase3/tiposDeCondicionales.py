#condicional simple

edad = int(input("Ingrese la edad: "))

if (edad > 18):
    print("Eres mayor de edad")



#condicional compuesta

nota = float(input("Ingrese la nota: "))

if(nota >= 3):
    print("aprobaste")
else:
    print("reprobaste")
    
    
    
#condicional multiple
nota = float(input("Ingrese la nota: "))
if nota >= 0 and nota < 3:
    print("reprobaste")
elif nota >= 3 and nota >= 5:
    print("aprobaste")
else:
    print("Error")
    

#condicional anidada
usuario = input("ingrese el usuario: ")
clave = input("ingrese la clave: ")

if usuario == "root":
    if clave == "admin":
        print("Bienvenido al home de la app")
    else:
        print("password incorrecto")
else:
    print("usuario no encontrado")


