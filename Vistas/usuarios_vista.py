from Controladores.usuarios_controlador import UsuarioControlador
from Modelos.usuario_modelo import UsuarioModelo
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui, QtCore
from interfaces.SITHome_LoginAdmin import Ui_MainWindow as Admin
from Vistas.dispositivos_vista import DispositivosUi

class UsuariosUi(QMainWindow):
        def __init__(self):
                super(UsuariosUi, self).__init__()
                self.loginAdmin = Admin()
                self.loginAdmin.setupUi(self)
                self.dispositivos = DispositivosUi()
                self.usuarioC = UsuarioControlador()
                self.inicialize()

        def inicialize(self):
                # botones SIT--------------------------------------------------------------------------

                # self.home.login.clicked.connect(lambda: self.SITHome_Login())

                self.loginAdmin.registerButton.setEnabled(False)
                self.loginAdmin.registerButton.clicked.connect(lambda: self.SITHome_register())
                self.loginAdmin.viewPass.clicked.connect(lambda: self.viewPass())
                self.loginAdmin.dispButton.clicked.connect(lambda: UsuariosUi().allDevs())
                self.loginAdmin.nameRegister.textChanged.connect(self.habilitarBtn)
                self.loginAdmin.codeRegister.textChanged.connect(self.habilitarBtn)
                

                # self.checkStatus('Puerta')
                # self.checkStatus('Luz')

                # self.devices.ui.doorSwitch.clicked.connect(lambda: self.changeStatus('Puerta'))
                # self.devices.ui.lightSwitch.clicked.connect(lambda: self.changeStatus('Luz'))
                self.dispositivos.listaDispositivos.back.clicked.connect(lambda: self.dispositivos.hide())
                self.dispositivos.listaDispositivos.back.clicked.connect(lambda: UsuariosUi().show())


        def showUsers(self):
                self.loginAdmin.userTable.clearContents()
                registredUsers = self.usuarioC.mostrarUsuario()
                row = 0
                for user in registredUsers:
                        column = 0
                        self.loginAdmin.userTable.removeRow(row)
                        self.loginAdmin.userTable.insertRow(row)
                        for element in user:
                                cell = QtWidgets.QTableWidgetItem(element)
                                self.loginAdmin.userTable.setItem(row, column, cell)
                                column +=1
                        row +=1

        def SITHome_register(self):
                newUsuario = UsuarioModelo()
                newUsuario.setNombreU(self.loginAdmin.nameRegister.text())
                newUsuario.setcontrasena(self.loginAdmin.codeRegister.text())
                if self.loginAdmin.adminCheck.isChecked():
                        typpe = 1
                else:
                        typpe = 2
                newUsuario.setRolU(typpe)
                self.loginAdmin.nameRegister.setText("")
                self.loginAdmin.codeRegister.setText("")
                self.usuarioC.crearUsuario(newUsuario)
                self.showUsers()
                self.habilitarBtn()

        def viewPass(self):
                self.loginAdmin.codeRegister.setEchoMode(0)

        def allDevs(self):
                # self.checkStatus("Puerta")
                # self.checkStatus("Luz")
                UsuariosUi().hide()
                self.dispositivos.show()
        def habilitarBtn(self):
                if (len(self.loginAdmin.codeRegister.text()) != 0 and len(self.loginAdmin.nameRegister.text()) != 0):
                        self.loginAdmin.registerButton.setEnabled(True)
                else:
                        self.loginAdmin.registerButton.setEnabled(False)