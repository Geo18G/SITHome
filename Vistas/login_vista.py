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
        globales.Usuario = None
        globales.idHabitaciones = None
        # self.habitaciones.habitaciones.btn_salir.clicked.connect(lambda: print(1))
        # globales.idUsuarios = None

    def regresarLogin(self):
        print(1)
        self.habitaciones.close()
        self.show()

    def SITHome_Login(self):
        usuario = self.home.loginCode_2.text()
        contrasena = self.home.loginCode.text()
        usuario = self.usuarioC.buscarUsuario(usuario,contrasena)
        if usuario:
            globales.Usuario = usuario

            # globales.idHabitaciones = self.habitacionC.obtener_ids()
            if usuario[2] == "Administrador":
                # globales.idUsuarios= self.usuarioC.obtener_ids()
                self.close()
                self.loginAdmin.show()
                globales.Habitaciones = self.habitacionC.obtener_Habitaciones()
                self.loginAdmin.showUsers()
            else:
                self.close()
                self.habitaciones.show()
                try:
                    self.habitaciones.showRooms()
                except:
                    pass
        else:
            self.home.loginCode.setStyleSheet("border-radius: 10px; border: 2px solid red; font: 24px;")
            self.home.loginCode_2.setStyleSheet("border-radius: 10px; border: 2px solid red; font: 24px;")
