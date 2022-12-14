from interfaces.SITHome_HabForm import Ui_Dialog
from interfaces.SITHome_DispForm import Ui_DialogD
from interfaces.SITHome_Devices import Ui_SITHome_Dispositivos
from interfaces.SITHome_Home import Ui_MainWindow
from interfaces.SITHome_LoginAdmin import Ui_SITHome_Usuarios
from PyQt5.QtWidgets import *
import sys
from passlib.context import CryptContext

# def singleton(clase):
#     instancias = dict()
    
#     def getInstancia(*args, **kwargs):
#         if clase not in instancias:
#             instancias[clase] = clase(*args, **kwargs)
#         return instancias[clase]
#     return getInstancia

# @singleton

class Formulario_Habitaciones(QDialog):
    def __init__(self):
        super(Formulario_Habitaciones, self).__init__()
        self.uiForm = Ui_Dialog()
        self.uiForm.setupUi(self)

class Formulario_Dispositivos(QDialog):
    def __init__(self):
        super(Formulario_Dispositivos, self).__init__()
        self.uiFormD = Ui_DialogD()
        self.uiFormD.setupUi(self)

class LoginUi(QMainWindow):
    def __init__(self):
        super(LoginUi, self).__init__()
        self.home = Ui_MainWindow()
        self.home.setupUi(self)

class UsuariosUi(QMainWindow):
    def __init__(self):
        super(UsuariosUi, self).__init__()
        self.usuarios = Ui_SITHome_Usuarios()
        self.usuarios.setupUi(self)

class HabitacionesUi(QMainWindow):
    def __init__(self):
        super(HabitacionesUi, self).__init__()
        self.habitaciones = Ui_SITHome_Dispositivos()
        self.habitaciones.setupUi(self)

class Plantilla():
    def __init__(self):
        self.home = LoginUi()
        self.usuarios = UsuariosUi()
        self.habitaciones = HabitacionesUi()
        self.addH = Formulario_Habitaciones()
        self.addD = Formulario_Dispositivos()
        self.contexto = CryptContext(
            schemes=["pbkdf2_sha256"],
            default="pbkdf2_sha256",
            pbkdf2_sha256__default_rounds=30000
        )



