

class DispositivosModelo:
    def __init__(self):
        self.nombre = str
        self.status = bool
        self.habitacion = str

    def setNombreD(self,nombre):
        self.nombre = nombre

    def setStatusD(self,status):
        self.status = status

    def setHabitacionD(self, habitacion):
        self.habitacion = habitacion

    def getNombred(self):
        return self.nombre

    def getStatus(self):
        return self.status

    def getHabitacionD(self):
        return self.habitacion

