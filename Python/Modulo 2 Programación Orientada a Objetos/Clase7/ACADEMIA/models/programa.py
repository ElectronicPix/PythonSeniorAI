class Programa:
    def __init__(self,id,nombre,cohorte):
        self.id = id
        self.nombre = nombre
        self.cohorte = cohorte
        
    def __str__(self):
        return f'{self.id}, {self.nombre}, {self.cohorte}'