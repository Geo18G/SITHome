from Controladores.usuarios_controlador import UsuarioControlador
from interfaces.SITHome_Home import Ui_MainWindow
from PyQt5.QtWidgets import *
from Vistas.dispositivos_vista import DispositivosUi
from Vistas.usuarios_vista import UsuariosUi

class LoginVista(QMainWindow):

    def __init__(self):
        super(LoginVista, self).__init__()
        self.home = Ui_MainWindow()
        self.home.setupUi(self)
        self.loginAdmin = UsuariosUi()
        self.dispositivos = DispositivosUi()
        self.usuarioC = UsuarioControlador()

        self.inicialize()

    def inicialize(self):
        # botones SIT--------------------------------------------------------------------------
        self.home.login.clicked.connect(lambda: self.SITHome_Login())

    def SITHome_Login(self):
        usuario = self.home.loginCode_2.text()
        print(usuario)
        contrasena = self.home.loginCode.text()
        print(contrasena)

        usuario = self.usuarioC.buscarUsuario(usuario,contrasena)
        if usuario:
            if usuario[3] == "Administrador":
                self.close()
                self.loginAdmin.show()
                self.loginAdmin.showUsers()
            else:
                self.close()
                self.dispositivos.show()
        else:
            self.home.loginCode.setStyleSheet("border-radius: 10px; border: 2px solid red; font: 24px;")

