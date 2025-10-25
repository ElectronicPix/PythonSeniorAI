from models.vehiculos import Parqueadero
from views.vista import VistaConsola

class ControladorParqueadero:
    
    def __init__(self):
        self._parqueadero = Parqueadero()
        self._vista = VistaConsola()
    
    def iniar_app(self):
        while True:
            self._vista.mostrar_menu_principal()
            opcion = self._vista.solicitar_opcion()
            
            if opcion == 1:
                self.ingresar_vehiculo()
            elif opcion == 2:
                self.retirar_vehiculo()
            elif opcion == 3:
                self.mostrar_estado_parqueadero()
            elif opcion == 4:
                self.mostrar_vehiculos_estacionados()
            elif opcion == 0:
                self._vista.despedida()
                break

    def ingresar_vehiculo(self):
        try:
            tipo = self._vista.pedir_tipo_vehiculo()
            
            if tipo is None:
                return
            
            placa = self._vista.pedir_placa()
            
            exito, mensaje = self._parqueadero.ingresar_vehiculo(tipo, placa)
            
            if exito:
                self._vista.mostrar_mensaje_exito(mensaje)
                
            else:
                print(mensaje)
        except Exception as e:
            self._vista.mostrar_error(str(e))
            
            
    def retirar_vehiculo(self):
        try:
            placa = self._vista.pedir_placa_retiro()
            
            vehiculo, costo = self._parqueadero.retirar_vehiculo(placa)
            
            if vehiculo is not False:
                self._vista.mostrar_ticket_salida(vehiculo, costo)
            else:
                self._vista.mostrar_error(vehiculo)
        except Exception as e:
            self._vista.mostrar_error(str(e))
            
            
def iniciar_app():
    controlador = ControladorParqueadero()
    controlador.iniar_app()