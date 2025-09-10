def calcuar_estadisticas(numeros):
    if not numeros:
        return "La lista está vacía"
    estadisticas = {
        "suma": sum(numeros), 
        "promedio": sum(numeros) / len(numeros), 
        "maximo": max(numeros), 
        "minimo": min(numeros), 
        "cantidad": len(numeros)
    }
    return estadisticas


numeros = [10, 23, 25, 69, 70, 90]
resultados = calcuar_estadisticas(numeros)
#print(resultados)

for resultado in resultados:
    print(f"{resultado} : {resultados[resultado]}")
    
#resutado: muestra la key 
#resultados[resultado]: muestra el value

for clave, valor in resultados.items(): # se usan los items para acceder.
    print(clave, valor)
