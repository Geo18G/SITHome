

class UsuarioModelo:
    def __init__(self):
        self.nombre = str
        self.contrasena = str
        self.rol = str

    def setNombreU(self,nombre):
        self.nombre = nombre

    def setcontrasena(self,contrasena):
        self.contrasena = contrasena

    def setRolU(self, rol):
        self.rol = rol

    def getRolU(self):
        return self.rol

    def getNombreU(self):
        return self.nombre

    def getContrasenaU(self):
        return self.contrasena