"""Supermercado - Total Compra"""

#Si compra solo el primer producto paga el 100%, si compra 2 productos el 70% y si compra los 3 productos el 65%

#declarar varibales y pedir datos por consola
print("Ingrese los precios de los tres productos")
producto1 = float(input("Precio del primer producto: "))
producto2 = float(input("Precio del segundo producto: "))
producto3 = float(input("Precio del tercer prooducto: "))

#aplicar operadores
total  = producto1 + producto2 + producto3

'''descuento = total * 0.35
totalPagar = total - descuento'''
#totalPagar = total * 0.65 # otra opción 

total *= 0.65 # solo el total a pagar, agilidad.

#imprimir datos por consola 
#print(f"el total a pagar es:  ${total} USD")
#print(f"el total es: ${total} USD, pero por llevar 3 productos su total a pagar con descuento es: {totalPagar}")

print(f"total a pagar es: {total}")

'''
La regla del descuento

En las instrucciones iniciales de tu código, se especifica lo siguiente:

1 producto: pagas el 100%.
2 productos: pagas el 70%. Esto significa que el descuento es del 30% (100 resta 70 = 30).
3 productos: pagas el 65%. Esto significa que el descuento es del 35%.
'''