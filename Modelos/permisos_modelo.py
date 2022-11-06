
class PermisoModelo:
    def __init__(self):
        self.permiso = bool
        self.id_usuario = int
        self.id_habitacion = int

    def setPermiso(self ,permiso):
        self.permiso = permiso

    def setIdUsuarioP(self, idU):
        self.id_usuario = idU

    def setIdHabitacionP(self, idH):
        self.id_habitacion = idH

    def getIdUsuarioP(self):
        return self.id_usuario

    def getIdHabitacionP(self):
        return self.id_habitacion

    def getPermiso(self):
        return self.permiso
