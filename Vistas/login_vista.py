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
        retorno = self.usuarioC.buscarUsuario(usuario)
        if retorno:
            correcto = self.contexto.verify(contrasena,retorno[3])
            if correcto:
                globales.Usuario = retorno
                if retorno[2] == "Administrador":
                    return True
                else:
                    return False
        else:
            self.home.home.sin_Conex.show()


