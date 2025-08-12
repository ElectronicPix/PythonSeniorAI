ventas = [
    ("V001", "Luis Rojas", 350000),
    ("V002", "Ana Torres", 580000),
    ("V003", "Carlos Díaz", 420000)
]

ventas_dict = {
    
    id_venta: {
        "cliente": cliente, 
        "monto": monto
    }
    for id_venta, cliente, monto in ventas
}

print("ventas registradas: ")
for id_venta, datos in ventas_dict.items():
    print("")