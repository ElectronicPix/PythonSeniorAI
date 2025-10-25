#Decoradores
#Acción a una función

def mayuscula(f):
  def envoltura(*arg, **kwargs):
    resultado = f(*arg, **kwargs)
    return resultado.upper()
  return envoltura

@mayuscula
def saludar(nombre):
  return f"Hola, {nombre}"

print(saludar("Juan"))



session = {
    "usuario_logueado": None
}

def login_required(f):
  def envoltura(*args, **kwargs):
    if session["usuario_logueado"]:
      print("Acceso concedido para ", session["usuario_logueado"])
      return f(*args, **kwargs)
    else:
      print("Acceso denegado")
      return None
  return envoltura

@login_required
def ver_panel_control():
  print("Panel de control")

ver_panel_control()