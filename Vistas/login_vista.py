from Controladores.usuarios_controlador import UsuarioControlador
import globales
from plantilla import Plantilla

class LoginVista(Plantilla):
    def __init__(self):
        super(LoginVista, self).__init__()
        self.usuarioC = UsuarioControlador()

    def SITHome_Login(self):
        usuario = self.home.home.loginCode_2.text()
        contrasena = self.home.home.loginCode.text()
        usuario = self.usuarioC.buscarUsuario(usuario,contrasena)
        if usuario:
            globales.Usuario = usuario
            if usuario[2] == "Administrador":
                return True
            else:
                return False
        else:
            pass


