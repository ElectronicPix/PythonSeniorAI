import datetime


class VistaConsola: # clase complementaria de control
    
    def mostrar_menu_principal(self):
        print("=== Menú Principal PARQUEADERO ===")
        print("1. Ingresar vehículo")
        print("2. Retirar vehículo")
        print("3. Consultar estado del parqueadero")
        print("4. Ver vehiculos estacionados")
        print("0. Salir")
        
    def solicitar_opcion(self):
        while True:
            try:
                opcion = input("Seleccione una opción: ")
                return int(opcion)
            except ValueError:
                print("Por favor, ingrese un número válido.")
                
    def mostrar_menu_tipo_vehiculo(self):
        print("Seleccione el tipo de vehículo:")
        print("1. Carro")
        print("2. Moto")
        print("3. Camion")
        print("0. Volver al menú principal")           
                
    def pedir_tipo_vehiculo(self):
        while True:
            self.mostrar_menu_tipo_vehiculo() # Componente de un mismo objeto (Clase)
            opcion = self.solicitar_opcion()
            
            if opcion == 1:
                return "Carro"
            elif opcion == 2:
                return "Moto"
            elif opcion == 3:
                return "Camion"
            elif opcion == 0:
                return None
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")
                
    def pedir_placa(self):
        while True:
            placa = input("Ingrese la placa del vehículo: ").strip().upper()
            if len(placa) == 6 and placa.isalnum():
                return placa
            else:
                print("Placa inválida. Debe tener 6 caracteres alfanuméricos.")
                
    def mostrar_mensaje(self, mensaje):
        print(f" ✔ {mensaje} ")
        
    def mostrar_error(self, mensaje):
        print(f" ✘ ERROR: {mensaje} ")
        
    def mostrar_mensaje_informativo(self, mensaje):
        print(f" ℹ {mensaje} ")
        
    def mostrar_estado_parqueadero(self, estado):
        print("=== Estado del Parqueadero ===")
        for tipo, info in estado.items():
            tipo_nombre = tipo.capitalize()
            print(f"{tipo_nombre}: {info['ocupados']} ocupados, {info['disponibles']} disponibles")
        print("==============================")
        
    def mostrar_vehiculos_estacionados(self, vehiculos):
        if not vehiculos:
            print("No hay vehículos estacionados.")
            return
        
        for placa, vehiculo in vehiculos.items():
            hora_entrada = vehiculo.horaEntrada.strftime("%I:%M:%S:%p")
            espacio = vehiculo.espacioAsignado
            
            print(f"Placa: {placa}, Hora de Entrada: {hora_entrada}, Espacio Asignado: {espacio}")
            
    
    def mostrar_ticket_salida(self, vehiculo, costo):
        print("=== Ticket de Salida ===")
        print(f"Placa: {vehiculo.placa}")
        print(f"Tipo: {vehiculo.tipo}")
        
        if vehiculo.horaEntrada:
            hora_entrada = vehiculo.horaEntrada.strftime("%I:%M:%S:%p")
            print(f"Entrada: {hora_entrada}")
            
        if vehiculo.horaEntrada:
            hora_salida = vehiculo.horaSalida.strftime("%I:%M:%S:%p")
            print(f"Salida: {hora_salida}")
            
        if vehiculo.horaEntrada and vehiculo.horaSalida:
            duracion = vehiculo.horaSalida - vehiculo.horaEntrada
            horas = duracion.total_seconds() / 3600
            print(f"Duración: {horas:.2f} horas")
            
        print(f"Costo Total: ${costo:.2f}")
        
    
    def despedida(self):
        print("Gracias por usar el sistema del parqueadero. ¡Hasta luego!")
        
        
        
    def pedir_placa_retiro(self):
        return input("Ingrese la placa del vehículo a retirar: ").strip().upper()