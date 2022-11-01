from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui, QtCore
from HomeUi import Ui_MainWindow
from DevicesUi import Ui_SITHome_Dispositivos 
from LoginAdminUi import Ui_MainWindow as Admin
import database as DB
import sys, os

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
        
        def inicialize(self):
        #botones SIT--------------------------------------------------------------------------
                
                self.home.login.clicked.connect(lambda: self.SITHome_Login())

                self.loginAdmin.ui.registerButton.clicked.connect(lambda: self.SITHome_register())
                self.loginAdmin.ui.viewPass.clicked.connect(lambda: self.viewPass())
                self.loginAdmin.ui.dispButton.clicked.connect(lambda: self.allDevs())
                
                self.checkStatus('Puerta')
                self.checkStatus('Luz')
                
                self.devices.ui.doorSwitch.clicked.connect(lambda: self.changeStatus('Puerta'))
                self.devices.ui.lightSwitch.clicked.connect(lambda: self.changeStatus('Luz'))
                self.devices.ui.back.clicked.connect(lambda: self.devices.hide())
                self.devices.ui.back.clicked.connect(lambda: self.loginAdmin.show())
                

        def SITHome_Login(self):
                code = self.home.loginCode.text()
                if DB.database.select_code(code):
                        if DB.database.is_admin(code)== 'Administrador':
                                self.hide()
                                self.loginAdmin.show()
                                self.showUsers()

                        elif DB.database.is_admin(code)== 'Usuario':
                                self.close()
                                self.devices.show()       
                else:
                        self.home.loginCode.setStyleSheet("border-radius: 10px; border: 2px solid red; font: 24px;")

        def showUsers(self):
                registredUsers = DB.database.select_all_users()
                self.loginAdmin.ui.userTable.clearContents()
                row = 0
                for user in registredUsers:
                        column = 0
                        self.loginAdmin.ui.userTable.insertRow(row)
                        for element in user:
                                cell = QtWidgets.QTableWidgetItem(element)
                                self.loginAdmin.ui.userTable.setItem(row, column, cell)
                                column +=1
                        row +=1
        def SITHome_register(self):
                name = self.loginAdmin.ui.nameRegister.text()
                code= self.loginAdmin.ui.codeRegister.text()
                regButton = self.loginAdmin.ui.registerButton
                if self.loginAdmin.ui.adminCheck.isChecked():
                        typpe = 'Administrador'
                else: 
                        typpe = 'Usuario'
                self.loginAdmin.ui.nameRegister.setText("")
                self.loginAdmin.ui.codeRegister.setText("")
                regButton.setText("Listo")
                regButton.setIcon(QtGui.QIcon("assets\ok.png"))
                regButton.setCursor(QtCore.Qt.ArrowCursor)
                regButton.setStyleSheet("QpushButton{background: None; font: 12pt; border: None;}")
                DB.database.insert_user(name, code, typpe)
                self.showUsers()
                
        def viewPass(self):
                self.loginAdmin.ui.codeRegister.setEchoMode(0)


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

        def backFromDevices(self):
                pass
                
if __name__=="__main__":
        app = QApplication([])
        myapp = SITHome()
        myapp.show()
        sys.exit(app.exec_())