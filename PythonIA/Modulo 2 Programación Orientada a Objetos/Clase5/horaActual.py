# Contenido de mi_fecha.py

from datetime import datetime

tiempo_actual = datetime.now()
fecha_formateada = tiempo_actual.strftime("%H:%M:%S")
fecha_Ahora = tiempo_actual.strftime("%I:%M:%S:%p  %A %B")


print("Hora actual:", fecha_Ahora)
print("Hora actual formateada:", fecha_formateada)
print(tiempo_actual) # Para ver el resultado

# Se continuo el proyecto del parqueadero
# Se creo la clase Vehiculo y Carro en el archivo vehiculos.py



# https://docs.python.org/3.6/library/datetime.html