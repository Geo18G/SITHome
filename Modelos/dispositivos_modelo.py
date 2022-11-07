

class DispositivoModelo:
    def __init__(self):
        self.nombre = str
        self.status = int
        self.habitacion = int

    def setNombreD(self,nombre):
        self.nombre = nombre

    def setStatusD(self,status):
        self.status = status

    def setHabitacionD(self, habitacion):
        self.habitacion = habitacion

    def getNombreD(self):
        return self.nombre

    def getStatus(self):
        return self.status

    def getHabitacionD(self):
        return self.habitacion

