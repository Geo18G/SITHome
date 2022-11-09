from Controladores.usuarios_controlador import UsuarioControlador
from interfaces.SITHome_Home import Ui_MainWindow
from PyQt5.QtWidgets import *
from Vistas.habitaciones_vista import HabitacionesUi
from Vistas.usuarios_vista import UsuariosUi
from Controladores.habitaciones_controlador import HabitacionControlador
import globales

class LoginVista(QMainWindow):

    def __init__(self):
        super(LoginVista, self).__init__()
        self.home = Ui_MainWindow()
        self.home.setupUi(self)
        self.loginAdmin = UsuariosUi()
        self.habitaciones = HabitacionesUi()
        self.habitacionC = HabitacionControlador()
        self.usuarioC = UsuarioControlador()
        self.inicialize()

    def inicialize(self):

        self.home.login.clicked.connect(lambda: self.SITHome_Login())
        # global idUsuario, idHabitaciones
        globales.idUsuario = 0
        globales.idHabitaciones = None
        #self.home.login.

    def SITHome_Login(self):
        usuario = self.home.loginCode_2.text()
        print(usuario)
        contrasena = self.home.loginCode.text()
        print(contrasena)
        usuario = self.usuarioC.buscarUsuario(usuario,contrasena)
        if usuario:
            # global idUsuario, idHabitaciones
            globales.idUsuario = usuario[0]
            globales.idHabitaciones = self.habitacionC.obtener_ids()
            if usuario[3] == 1:
                self.close()
                self.loginAdmin.show()
                self.loginAdmin.showUsers()
            else:
                self.close()
                self.habitaciones.show()
                self.habitaciones.showRooms()
        else:
            self.home.loginCode.setStyleSheet("border-radius: 10px; border: 2px solid red; font: 24px;")

