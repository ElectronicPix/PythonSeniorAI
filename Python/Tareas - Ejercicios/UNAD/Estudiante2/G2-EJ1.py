class Banco:
    def __init__(self, balance):
        self._balance = balance
    def depostar(self, cantidad):
        self._balance += cantidad
        return f"Depositaste ${cantidad} y tu saldo actual es ${self._balance}"
    def retirar(self, cantida):
        if cantida <= self._balance:
            self._balance -= cantida
            return f"Retiraste ${cantida} saldo actual es ${self._balance}"
        else:
            return f"No se puede retirar ${cantida} su saldo es ${self._balance}"


cliente1 = Banco(300)
print(cliente1.depostar(200))
print(cliente1.retirar(100))
print(cliente1.retirar(600)) # Saldo erroneo