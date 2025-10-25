def calcular_area_rectangulo(base: float, altura: float)->float:
  '''
  Calcula el área de un rectángulo.

  Param: base: float
  Param: altura: float
  Return: float
  '''
  return base * altura

def calcular_area_rectangulo(base, altura): # Retorno de valores
  return base * altura # Permite almacenar el valor para luego usarlo en una variable, u otro lugar.


def calcular_area_rectanguloc(base, altura): # Sin retorno de valores
  print("El área del rectángulo es:", base * altura)

area1 = calcular_area_rectangulo(15.3, 10.4)
area2 = calcular_area_rectangulo(12.3, 14.7)

print("El área del rectángulo es:", area1)
print("El área del rectángulo es:", area2)
calcular_area_rectanguloc(15.3, 10.4)