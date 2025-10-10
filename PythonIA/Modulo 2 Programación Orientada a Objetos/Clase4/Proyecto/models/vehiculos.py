import datetime

class Vehiculo:
    """
    Clase base que representa un vehículo genérico en el estacionamiento.
    """
    
    def __init__(self, tipo, altura, placa):
        """
        Inicializa un objeto Vehiculo.

        Args:
            tipo (str): El tipo de vehículo (ej. "Carro", "Moto").
            altura (float): La altura del vehículo en metros.
            placa (str): La placa del vehículo.
        """
        self._tipo = tipo
        self._altura = altura
        self._placa = placa
        self._horaEntrada = None  # La hora de entrada se establecerá al ingresar al parqueadero.
        self._horaSalida = None   # La hora de salida se establecerá al salir del parqueadero.
        self._espacioAsignado = None # El espacio de estacionamiento asignado.
        
    @property
    def tipo(self):
        """Obtiene el tipo del vehículo."""
        return self._tipo
    
    @property
    def altura(self):
        """Obtiene la altura del vehículo."""
        return self._altura

    @property
    def placa(self):
        """Obtiene la placa del vehículo."""
        return self._placa
    
    @property
    def horaEntrada(self):
        """Obtiene la hora de entrada del vehículo."""
        return self._horaEntrada
    
    @horaEntrada.setter
    def horaEntrada(self, horaEntrada):
        self.horaEntrada = horaEntrada
    
    @property
    def horaSalida(self):
        """Obtiene la hora de salida del vehículo."""
        return self._horaSalida
    
    @horaSalida.setter
    def horaSalida(self, horaSalida):
        self.horaSalida = horaSalida
    
    @property
    def espacioAsignado(self):
        """Obtiene el espacio de estacionamiento asignado al vehículo."""
        return self._espacioAsignado
    
    @espacioAsignado.setter
    def espacioAsignado(self, espacioAsignado):
        self.espacioAsignado = espacioAsignado
        
            
class Carro(Vehiculo):
    """
    Clase que representa un Carro, hereda de Vehiculo.
    """
    def __init__(self, tipo, altura, placa):
        """
        Inicializa un objeto Carro con valores predeterminados para tipo y altura.
        """
        super().__init__("Carro", 1.6, placa)
        
        
class Moto(Vehiculo):
    """
    Clase que representa una Moto, hereda de Vehiculo.
    """
    def __init__(self, tipo, altura, placa):
        """
        Inicializa un objeto Moto con valores predeterminados para tipo y altura.
        """
        super().__init__("Moto", 1.2, placa)
        
class Camion(Vehiculo):
    """
    Clase que representa un Camión, hereda de Vehiculo.
    """
    def __init__(self, tipo, altura, placa):
        """
        Inicializa un objeto Camion con valores predeterminados para tipo y altura.
        """
        super().__init__("Camion", 3.0, placa)
    
class FabricaVehiculos:
    """
    Clase que implementa el patrón de diseño Factory para crear objetos de tipo Vehiculo.
    """
    
    @staticmethod
    def crear(tipo, placa):
        """
        Crea y devuelve una instancia de un vehículo específico basado en el tipo.

        Args:
            tipo (str): El tipo de vehículo a crear ("carro", "moto", "camion").
            placa (str): La placa del vehículo.

        Returns:
            Vehiculo: Una instancia de Carro, Moto o Camion.

        Raises:
            ValueError: Si el tipo de vehículo no es válido.
        """
        if tipo == "carro":
            return Carro(placa)
        elif tipo == "moto":
            return Moto(placa)
        elif tipo == "camion":
            return Camion(placa)
        else:
            raise ValueError("Tipo de vehiculo no valido")
        
        
# Tarea: relizar patron de comportamiento de responsabilidad.



class CalcularTarifa:
    """
    Clase responsable de calcular el costo del estacionamiento para un vehículo.
    """
    
    def __init__(self):
        """
        Inicializa el calculador de tarifas con las tarifas por tipo de vehículo.
        """
        self._tarifa = {
            "carro": 2000, 
            "moto": 1000, 
            "camion": 5000
        }
        
        
    def calcular_costo(self, Vehiculo, horaEntrada, horaSalida):
        """
        Calcula el costo total del estacionamiento basado en la duración y el tipo de vehículo.

        Args:
            Vehiculo (Vehiculo): El objeto vehículo.
            horaEntrada (datetime): La hora de entrada del vehículo.
            horaSalida (datetime): La hora de salida del vehículo.

        Returns:
            float: El costo total del estacionamiento. Retorna 0 si las horas no son válidas.
        """
        
        if not horaEntrada or not horaSalida:
            return 0

        # Calcula la duración en horas.
        duracion = horaSalida - horaEntrada
        horas = duracion.total_seconds() / 3600
        
        # Se cobra como mínimo una hora.
        horas = max(1, horas)
        
        # Obtiene el tipo de vehículo y calcula el costo.
        tipo = Vehiculo.tipo.lower()
        return self._tarifa[tipo] * horas
    
    

class GestorEspacios:
    """
    Clase que gestiona los espacios de estacionamiento disponibles.
    """
    def __init__(self):
        """
        Inicializa el gestor de espacios con la cantidad de espacios por tipo de vehículo.
        """
        self._espacios = {
            "carro":  20,
            "moto":   30,
            "camion": 5
        }
        
        
    def hay_espacios_disonobles(self, tipo):
        """
        Verifica si hay espacios disponibles para un tipo de vehículo.

        Args:
            tipo (str): El tipo de vehículo.

        Returns:
            bool: True si hay espacios disponibles, False en caso contrario.
        """
        return self._espacios[tipo]
    
    
    def asignar_espacio(self, Vehiculo):
        """
        Asigna un espacio de estacionamiento a un vehículo.

        Args:
            Vehiculo (Vehiculo): El vehículo al que se le asignará el espacio.

        Returns:
            bool: True si se pudo asignar el espacio, False en caso contrario.
        """
        tipo = Vehiculo.tipo.lower()
        
        
        if not self.hay_espacios_disonobles(tipo):
            return False
        
        self._espacios[tipo] -= 1
        return True
    
    def liberar_espacio(self, vehiculo):
        """
        Libera un espacio de estacionamiento.

        Args:
            Vehiculo (Vehiculo): El vehículo que ocupaba el espacio.

        Returns:
            bool: True si se pudo liberar el espacio.
        """
        tipo = Vehiculo.tipo.lower()
        self._espacios[tipo] += 1
        return True
        
    
    
    
    
class RepositorioVehiculos:
    """
    Clase que gestiona el almacenamiento y la recuperación de vehículos en el parqueadero.
    """
    
    def __init__(self):
        """
        Inicializa el repositorio de vehículos.
        """
        self._Vehiculos = {}
        
    def guardar(self, Vehiculos):
        """
        Guarda un vehículo en el repositorio.

        Args:
            Vehiculos (Vehiculo): El vehículo a guardar.
        """
        self._Vehiculos[Vehiculo.placa] = Vehiculo
        
    def obtener(self, placa):
        """
        Obtiene un vehículo del repositorio por su placa.

        Args:
            placa (str): La placa del vehículo.

        Returns:
            Vehiculo: El vehículo si se encuentra, None en caso contrario.
        """
        return self._Vehiculos.get(placa)
    
    def eliminar(self, placa):
        """
        Elimina un vehículo del repositorio por su placa.

        Args:
            placa (str): La placa del vehículo.

        Returns:
            bool: True si se eliminó el vehículo, False en caso contrario.
        """
        if placa in self._Vehiculos[placa]:
            del self._Vehiculos[placa]
            return True
        return False
    
    def obtener_todos(self):
        """
        Obtiene todos los vehículos del repositorio.

        Returns:
            dict: Un diccionario con todos los vehículos.
        """
        return self._Vehiculos.copy()
    
    def existe_placa(self, placa):
        """
        Verifica si ya existe un vehículo con una placa dada.

        Args:
            placa (str): La placa a verificar.

        Returns:
            bool: True si la placa ya existe, False en caso contrario.
        """
        return placa in self._Vehiculos
    
    
class Parqueadero:
    """
    Clase principal que gestiona el parqueadero.
    """
    
    def __init__(self):
        """
        Inicializa el parqueadero con sus componentes.
        """
        self._fabrica = FabricaVehiculos()
        self._calculadora = CalcularTarifa()
        self._gestor_espacios = GestorEspacios()
        self._repositorio = RepositorioVehiculos()
        
        
    def ingresar_vehiculo(self, tipo, placa):
        """
        Ingresa un vehículo al parqueadero.

        Args:
            tipo (str): El tipo de vehículo.
            placa (str): La placa del vehículo.

        Returns:
            tuple: Una tupla con un booleano indicando si la operación fue exitosa y un mensaje.
        """
        try:
            if not self._gestor_espacios.hay_espacios_disonobles(tipo):
                return False, f"No hay espacio disponible para {tipo}"
            
            if self._repositorio.existe_placa(placa):
                return False, f"El vehiculo con placa {placa} ya se encuentra registrado"
            
            vehiculo = self._fabrica.crear(tipo, placa)
            
            espacio = self._gestor_espacios.asignar_espacio(Vehiculo)
            
            if espacio is False:
                return False, f"No hay espacios disponibles para {tipo} "
            
            Vehiculo.horaEntrada = datetime.datetime.now()
            
            return True, f"Vhiculo {tipo}, con placa {placa} ingresado exitosamente"
        
        except Exception as e:
            return False, str(e)
            
    def retirar_vehiculo(self, placa):
        """
        Retira un vehículo del parqueadero.

        Args:
            placa (str): La placa del vehículo a retirar.

        Returns:
            tuple: Una tupla con el vehículo y el costo, o un booleano y un mensaje de error.
        """
        try:
            vehiculo = self._repositorio.obtener_por_placa(placa)
            if not Vehiculo:
                return False, f"El vehiculo con placa {placa} no se encuentra en el parqueadero"
            
            vehiculo_liberado = self._gestor_espacios.liberar_espacio(Vehiculo)
            if vehiculo_liberado is False:
                return False, f"No se pudo liberar el espacio para el vehiculo con placa {placa}"
            
            Vehiculo.horaSalida = datetime.datetime.now()
            costo = self._calculadora.calcular_costo(Vehiculo, Vehiculo.horaEntrada, Vehiculo.horaSalida)
            
            self._repositorio.eliminar(placa)
            return vehiculo, costo
        
        except Exception as e:
            return False, str(e)
    
    def consultar_estado(self):
        """
        Consulta el estado actual del parqueadero.

        Returns:
            dict: Un diccionario con todos los vehículos en el parqueadero.
        """
        return self._repositorio.obtener_todos()
    
    def obtener_vehiculo_por_placa(self, placa):
        """
        Obtiene un vehículo por su placa.

        Args:
            placa (str): La placa del vehículo.

        Returns:
            Vehiculo: El vehículo si se encuentra, None en caso contrario.
        """
        return self._repositorio.obtener_vehiculo_por_placa(placa)

            
# 1 h 44 min 10 seg