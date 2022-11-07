from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui, QtCore
from interfaces.SITHome_Home import Ui_MainWindow
from interfaces.SITHome_Devices import Ui_SITHome_Dispositivos
from interfaces.SITHome_LoginAdmin import Ui_MainWindow as Admin
import database as DB
from Vistas.login_vista import LoginVista
import sys
from Controladores.usuarios_controlador import UsuarioControlador
from Modelos.usuario_modelo import UsuarioModelo

class DevicesUi(QMainWindow):
        def __init__(self):
                super(DevicesUi, self).__init__()
                self.ui = Ui_SITHome_Dispositivos()
                self.ui.setupUi(self)

class AdminUi(QMainWindow):
        def __init__(self):
                super(AdminUi, self).__init__()
                self.ui = Admin()
                self.ui.setupUi(self)

class SITHome(QMainWindow):
        def __init__(self):
                super(SITHome, self).__init__()
                self.home = Ui_MainWindow()
                self.home.setupUi(self)
                self.devices = DevicesUi()
                self.loginAdmin = AdminUi()
                self.inicialize()
#
        def inicialize(self):
        #botones SIT--------------------------------------------------------------------------

                self.home.login.clicked.connect(lambda: self.SITHome_Login())

                self.loginAdmin.ui.registerButton.clicked.connect(lambda: self.SITHome_register())
                self.loginAdmin.ui.viewPass.clicked.connect(lambda: self.viewPass())
                self.loginAdmin.ui.dispButton.clicked.connect(self.allDevs)

                self.checkStatus('Puerta')
                self.checkStatus('Luz')

                self.devices.ui.doorSwitch.clicked.connect(lambda: self.changeStatus('Puerta'))
                self.devices.ui.lightSwitch.clicked.connect(lambda: self.changeStatus('Luz'))
                self.devices.ui.back.clicked.connect(lambda: self.devices.hide())
                self.devices.ui.back.clicked.connect(lambda: self.loginAdmin.show())
#
#
#         def SITHome_Login(self):
#                 code = self.home.loginCode.text()
#                 print(type(code))
#                 usuarioC = UsuarioControlador()
#                 usuario = usuarioC.buscarUsuario(code)
#                 print(usuario)
#                 if usuario:
#                         if usuario[3] == 1:
#                                 self.hide()
#                                 self.loginAdmin.show()
#                                 self.showUsers()
#                         else:
#                                 self.close()
#                                 self.devices.show()
#                 else:
#                         self.home.loginCode.setStyleSheet("border-radius: 10px; border: 2px solid red; font: 24px;")
#
#         def showUsers(self):
#                 usuarioC = UsuarioControlador()
#                 registredUsers = usuarioC.mostrarUsuario()
#                 self.loginAdmin.ui.userTable.clearContents()
#                 row = 0
#                 for user in registredUsers:
#                         column = 0
#                         self.loginAdmin.ui.userTable.insertRow(row)
#                         for element in user:
#                                 cell = QtWidgets.QTableWidgetItem(element)
#                                 self.loginAdmin.ui.userTable.setItem(row, column, cell)
#                                 column +=1
#                         row +=1
#
#         def SITHome_register(self):
#                 usuarioC = UsuarioControlador()
#                 newUsuario = UsuarioModelo()
#                 newUsuario.setNombreU(self.loginAdmin.ui.nameRegister.text())
#                 newUsuario.setcontrasena(self.loginAdmin.ui.codeRegister.text())
#                 regButton = self.loginAdmin.ui.registerButton
#                 if self.loginAdmin.ui.adminCheck.isChecked():
#                         typpe = 1
#                 else:
#                         typpe = 2
#                 newUsuario.setRolU(typpe)
#                 self.loginAdmin.ui.nameRegister.setText("")
#                 self.loginAdmin.ui.codeRegister.setText("")
#                 regButton.setText("Listo")
#                 regButton.setIcon(QtGui.QIcon("assets\ok.png"))
#                 regButton.setCursor(QtCore.Qt.ArrowCursor)
#                 regButton.setStyleSheet("QpushButton{background: None; font: 12pt; border: None;}")
#                 usuarioC.crearUsuario(newUsuario)
#                 self.showUsers()
#
#         def viewPass(self):
#                 self.loginAdmin.ui.codeRegister.setEchoMode(0)
#

        def allDevs(self):
                self.checkStatus("Puerta")
                self.checkStatus("Luz")
                self.loginAdmin.hide()
                self.devices.show()

        def checkStatus(self, device):
                off = "assets\interruptor-off.png"
                on  = "assets\interruptor-on.png"
                if device == "Puerta":
                        devicePointer = self.devices.ui.doorSwitch
                elif device == "Luz":
                        devicePointer = self.devices.ui.lightSwitch
                status = DB.database.checkStatusDB(device)
                if status == 'ON':
                        devicePointer.setIcon(QtGui.QIcon(on))
                elif status == 'OFF':
                        devicePointer.setIcon(QtGui.QIcon(off))

        def changeStatus(self, device):
                DB.database.changeStatusDB(device)
                self.checkStatus(device)
#
#         def backFromDevices(self):
#                 pass
#
if __name__=="__main__":
        app = QApplication([])
        myapp = LoginVista()
        myapp.show()
        sys.exit(app.exec_())