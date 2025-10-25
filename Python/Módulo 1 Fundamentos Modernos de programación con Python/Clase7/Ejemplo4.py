#Función Lambda(Anonimas)
#Sintaxis lambda argumentos: expresión
calcularAreaRectangulo = lambda base, altura: base * altura
area3 = calcularAreaRectangulo(15.3, 10.4)
print("El área del rectángulo es:", area3)



#Funciones como argumentos
def operar(f, x, y):
  return f(x, y)

def multiplicar(a, b):
  return a * b

print(operar(multiplicar, 10, 5))

