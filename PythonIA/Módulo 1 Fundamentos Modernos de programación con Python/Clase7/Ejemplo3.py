def manejar(edad, licencia = False): # Función con parametro, parametro por defecto( licencia = false).
  if edad >= 18 and licencia:
    print("Puedes conducir")
  elif edad >= 18 and not licencia:
    print("Necesitas una licencia")
  else:
    print("Eres menor de edad")

manejar(17)# No está oligado a cumplir el otro parametro ya que es por defecto.
manejar(18, True)