from Controladores.usuarios_controlador import UsuarioControlador
from interfaces.SITHome_Home import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui, QtCore
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

        # self.loginAdmin.ui.registerButton.clicked.connect(lambda: self.SITHome_register())
        # self.loginAdmin.ui.viewPass.clicked.connect(lambda: self.viewPass())
        # self.loginAdmin.ui.dispButton.clicked.connect(lambda: self.allDevs())

        # self.checkStatus('Puerta')
        # self.checkStatus('Luz')

        # self.dispositivos.ui.doorSwitch.clicked.connect(lambda: self.changeStatus('Puerta'))
        # self.dispositivos.ui.lightSwitch.clicked.connect(lambda: self.changeStatus('Luz'))
        # self.dispositivos.ui.back.clicked.connect(lambda: self.dispositivos.hide())
        # self.dispositivos.ui.back.clicked.connect(lambda: self.loginAdmin.show())

    # def viewPass(self):
    #     self.loginAdmin.ui.codeRegister.setEchoMode(0)

    def SITHome_Login(self):
        code = self.home.loginCode.text()
        usuario = self.usuarioC.buscarUsuario(code)
        if usuario:
            if usuario[3] == 1:
                self.hide()
                self.loginAdmin.show()
                self.loginAdmin.showUsers()
            else:
                self.close()
                self.dispositivos.show()
        else:
            self.home.loginCode.setStyleSheet("border-radius: 10px; border: 2px solid red; font: 24px;")

    # def showUsers(self):
    #     usuarioC = UsuarioControlador()
    #     registredUsers = usuarioC.mostrarUsuario()
    #     self.loginAdmin.ui.userTable.clearContents()
    #     row = 0
    #     for user in registredUsers:
    #         column = 0
    #         self.loginAdmin.ui.userTable.insertRow(row)
    #         for element in user:
    #             cell = QtWidgets.QTableWidgetItem(element)
    #             self.loginAdmin.ui.userTable.setItem(row, column, cell)
    #             column += 1
    #         row += 1