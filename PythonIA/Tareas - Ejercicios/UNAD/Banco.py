class Banco:
    
    def __init__(self, saldo):
        self.saldo = saldo
        print(f"Saldo inicial: ${self.saldo}")
        
    def depositar(self, cantidad):
        self.saldo += cantidad
        return f"Se depositaron: ${cantidad}, saldo actual: ${self.saldo}"
    
    def retirar(self, cantidad):
        if cantidad > self.saldo:
            return "Fondo insuficiente"
        else: 
            self.saldo -= cantidad
            return f"Se retiraron: ${cantidad}, saldo actual: ${self.saldo}"
        
cliente1 = Banco(500) # saldo actual 
print(cliente1.depositar(500)) # deposito
print(cliente1.retirar(2000)) # No se pudo retirar
print(cliente1.retirar(100)) # Retiro exitoso