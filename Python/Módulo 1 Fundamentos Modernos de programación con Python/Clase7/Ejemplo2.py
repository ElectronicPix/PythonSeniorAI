''' Ejemplo 1'''

def mostrar_menu():
  print("MENU")
  print("1. OPCION 1")
  print("2. OPCION 2")
  print("3. OPCION 3")
  print("4. SALIR")

def menu():
  # No se pone las opciones de mostrar menu por temas de mantenimiento, reutilización de código.
  mostrar_menu()
  opcion = int(input("Ingrese una opción: "))
  return opcion

menu()