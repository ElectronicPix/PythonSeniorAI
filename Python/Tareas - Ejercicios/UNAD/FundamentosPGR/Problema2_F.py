"""Problema 2: Se gestionan los precios de un menú de restaurante. El menú se representa como una 
matriz: [Nombre del Producto, Categoría, Precio Base]. Se requiere una funcionalidad para aplicar una 
promoción a productos específicos. Requisitos de Desarrollo - Matriz: Crear una matriz con al menos 6 productos 
de diversas categorías. - Módulos: Se requiere un módulo (función) para calcular el precio final de un producto. 
- Lógica de Negocio: ✓ Aplicar un 15% de descuento si el producto cumple con la categoría objetivo, específica y 
su precio base es mayor a un umbral definido. ✓ Mantener el precio base si no se cumplen las condiciones. - Salida:
Mostrar cada producto, su precio base y el precio final con la promoción aplicada"""

# =================================================================
# Programa: Gestión de Precios y Promociones en Menú de Restaurante
# =================================================================

# 1. MÓDULOS (Funciones)
# Esta función calcula el precio final del producto según la lógica de negocio.
def calcular_precio_final(precio_base, categoria_producto, categoria_objetivo, umbral_precio):
    """
    Evalúa si un producto aplica para el 15% de descuento.
    Retorna el precio modificado o el precio base si no cumple.
    """
    # Verifica si es la categoría correcta y supera el umbral de precio
    if categoria_producto == categoria_objetivo and precio_base > umbral_precio:
        # Aplica un 15% de descuento
        descuento = precio_base * 0.15
        precio_final = precio_base - descuento
        return precio_final
    else:
        # Mantiene el precio base
        return precio_base

# 2. INICIALIZACIÓN DE VARIABLES Y MATRIZ
# Matriz del menú: [Nombre del Producto, Categoría, Precio Base]
menu_restaurante = [
    ["Hamburguesa Doble", "Platos Fuertes", 25000],
    ["Pizza Personal", "Platos Fuertes", 18000],
    ["Ensalada César", "Entradas", 12000],
    ["Gaseosa 400ml", "Bebidas", 4500],
    ["Jugo Natural", "Bebidas", 6000],
    ["Brownie con Helado", "Postres", 9000],
    ["Cheesecake", "Postres", 15000]
]

# Variables para la promoción actual
cat_promocion = "Platos Fuertes"
umbral_minimo = 15000
pedido_cliente = [] # Lista vacía para guardar lo que el cliente escoja

# 3. INTERACCIÓN CON EL USUARIO (El cliente escoge)
print("=" * 45)
print(" BIENVENIDO AL RESTAURANTE UNAD ")
print(f" ¡Hoy: 15% de descuento en {cat_promocion}")
print(f" para compras mayores a ${umbral_minimo}!")
print("=" * 45)

haciendo_pedido = True

while haciendo_pedido:
    print("\n--- MENÚ DISPONIBLE ---")
    # Mostramos los productos al cliente iterando sobre la matriz
    for i in range(len(menu_restaurante)):
        producto = menu_restaurante[i]
        # i+1 es para que el menú empiece en 1 y no en 0
        print(f"{i + 1}. {producto[0]} ({producto[1]}) - ${producto[2]}")
    
    print("0. Terminar pedido y pagar")
    
    # Capturamos la opción del cliente
    opcion = input("\nDigite el número del producto que desea pedir: ")
    
    if opcion == "0":
        haciendo_pedido = False # Rompe el ciclo
    elif opcion.isdigit():
        opcion_num = int(opcion)
        # Verificamos que el número esté dentro del menú
        if 1 <= opcion_num <= len(menu_restaurante):
            indice = opcion_num - 1
            producto_elegido = menu_restaurante[indice]
            # Agregamos el producto a la lista del pedido
            pedido_cliente.append(producto_elegido)
            print(f"-> ¡{producto_elegido[0]} agregado a tu orden!")
        else:
            print("Error: Número de producto no existe. Intente de nuevo.")
    else:
        print("Error: Por favor ingrese un número válido.")

# 4. SALIDA: CÁLCULO Y FACTURA FINAL
print("\n" + "=" * 45)
print("               FACTURA DE COMPRA              ")
print("=" * 45)

if len(pedido_cliente) == 0:
    print("No seleccionaste ningún producto. ¡Vuelve pronto!")
else:
    total_pagar = 0
    
    # Recorremos cada producto que el cliente escogió
    for item in pedido_cliente:
        nombre = item[0]
        categoria = item[1]
        precio_b = item[2]
        
        # Llamamos al módulo para calcular el precio
        precio_f = calcular_precio_final(precio_b, categoria, cat_promocion, umbral_minimo)
        
        # Sumamos al total de la cuenta
        total_pagar += precio_f
        
        # Mostramos la salida solicitada:
        print(f"Producto: {nombre}")
        print(f"Precio Base: ${precio_b}")
        if precio_f < precio_b:
            print(f"Precio Final: ${precio_f} (¡Promoción aplicada!)")
        else:
            print(f"Precio Final: ${precio_f}")
        print("-" * 25)
        
    print(f"TOTAL A PAGAR: ${total_pagar}")
print("=" * 45)