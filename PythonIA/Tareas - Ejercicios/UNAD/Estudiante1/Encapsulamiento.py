class Usuario:
    
    def __init__(self, passwod):
        self._password = passwod
        
    def cambiar_contrasena(self, contrasena_actual, nueva_contrasena):
        
        if contrasena_actual == self._password:
            self._password = nueva_contrasena
            print("¡Contraseña cambiada con exito! ✔")
            print(f"Su contraseña actual es: {self._password}")
        else:
            print("Error: La contraseña actual es incorrecta. ❌")

mi_usuario = Usuario('1234') # Contraseña inicial
mi_usuario.cambiar_contrasena('1234', '4566') # Verificación exitosa
mi_usuario.cambiar_contrasena('7869', '4566') # contraseña incorrecta