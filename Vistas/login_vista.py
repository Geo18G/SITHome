from Controladores.usuarios_controlador import UsuarioControlador
# from interfaces.SITHome_Home import Ui_MainWindow
from PyQt5.QtWidgets import *
# from Vistas.habitaciones_vista import HabitacionesVista
# from Vistas.usuarios_vista import UsuariosVista
from Controladores.habitaciones_controlador import HabitacionControlador
import globales
from plantilla import Plantilla
import sys

class LoginVista(Plantilla):
    def __init__(self):
        super(LoginVista, self).__init__()
        self.habitacionC = HabitacionControlador()
        self.usuarioC = UsuarioControlador()
        # self.habitacion = HabitacionesVista()
        # self.usuarios = UsuariosVista()
    #     self.inicialize()

    # def inicialize(self):
    #     self.home.home.login.clicked.connect(lambda: self.SITHome_Login())
    #     globales.Usuario = None
    #     globales.idHabitaciones = None

        # self.habitaciones.habitaciones.btn_salir.clicked.connect(lambda: print(1))
        # globales.idUsuarios = None

    # def regresarLogin(self):
    #     print(1)
    #     self.habitaciones.close()
    #     self.show()

    def SITHome_Login(self):
        usuario = self.home.home.loginCode_2.text()
        contrasena = self.home.home.loginCode.text()
        usuario = self.usuarioC.buscarUsuario(usuario,contrasena)
        if usuario:
            globales.Usuario = usuario
            if usuario[2] == "Administrador":
                # goToUser = UsuariosVista()
                # print(0)
                # self.home.close()
                # goToUser.usuarios.show()
                # print(1)
                globales.Habitaciones = self.habitacionC.obtener_Habitaciones()
                # print(2)
                # goToUser.showUsers()
                # print(3)
                return True

            else:
                # goToHab = HabitacionesVista()
                # self.home.close()
                # goToHab.habitaciones.show()
                # try:
                #     goToHab.showRooms()
                # except:
                #     pass
                return False


        else:
            self.home.home.loginCode.setStyleSheet("border-radius: 10px; border: 2px solid red; font: 24px; background-color: white;")
            self.home.home.loginCode_2.setStyleSheet("border-radius: 10px; border: 2px solid red; font: 24px; background-color: white;")


# if __name__=="__main__":
#         app = QApplication([])
#         myapp = UsuariosVista()
#         myapp.usuarios.show()
#         sys.exit(app.exec_())