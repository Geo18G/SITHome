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
                
                self.loginAdmin.registerButton.setEnabled(False)
                self.loginAdmin.registerButton.clicked.connect(lambda: self.SITHome_register())
                self.loginAdmin.viewPass.clicked.connect(lambda: self.viewPass())
                self.loginAdmin.dispButton.clicked.connect(lambda: UsuariosUi().allDevs())
                self.loginAdmin.nameRegister.textChanged.connect(lambda: self.habilitarBtn(self.loginAdmin.registerButton))
                self.loginAdmin.codeRegister.textChanged.connect(lambda: self.habilitarBtn(self.loginAdmin.registerButton))
                self.loginAdmin.nameRegister.textChanged.connect(lambda: self.habilitarBtn(self.loginAdmin.btnGuardar))
                self.loginAdmin.codeRegister.textChanged.connect(lambda: self.habilitarBtn(self.loginAdmin.btnGuardar))
                self.loginAdmin.btnGuardar.clicked.connect(self.editarUsuario)
                self.loginAdmin.btnGuardar.hide()
                
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
                        cell = QtWidgets.QTableWidgetItem(user[1])
                        self.loginAdmin.userTable.setItem(row, column, cell)
                        column +=1
                        cell = QtWidgets.QTableWidgetItem(user[2])
                        self.loginAdmin.userTable.setItem(row, column, cell)
                        self.agregarBtn(self.loginAdmin.userTable, row, user)
                        row +=1

        def SITHome_register(self):
                newUsuario = UsuarioModelo()
                newUsuario.setNombreU(self.loginAdmin.nameRegister.text())
                newUsuario.setContrasenaU(self.loginAdmin.codeRegister.text())
                if self.loginAdmin.adminCheck.isChecked():
                        typpe = 1
                else:
                        typpe = 2
                newUsuario.setRolU(typpe)
                self.loginAdmin.nameRegister.setText("")
                self.loginAdmin.codeRegister.setText("")
                self.usuarioC.crearUsuario(newUsuario)
                self.showUsers()
                self.habilitarBtn(self.loginAdmin.registerButton)

        def viewPass(self):
                self.loginAdmin.codeRegister.setEchoMode(0)

        def allDevs(self):
                UsuariosUi().hide()
                self.dispositivos.show()

        def habilitarBtn(self, btn):
                if (len(self.loginAdmin.codeRegister.text()) >=4 and len(self.loginAdmin.nameRegister.text()) !=0):
                        btn.setEnabled(True)
                else:
                        btn.setEnabled(False)
        
        def agregarBtn(self, tabla, fila, usuario):
                BtnBorrar = QtWidgets.QPushButton()
                BtnEditar = QtWidgets.QPushButton()
                tabla.setCellWidget(fila, 2, BtnEditar)
                tabla.setCellWidget(fila, 3, BtnBorrar)
                BtnEditar.setMaximumSize(28, 28)
                BtnBorrar.setMaximumSize(28, 28)                
                BtnEditar.setIcon(QtGui.QIcon("assets\\btnEditar.png"))
                BtnBorrar.setIcon(QtGui.QIcon("assets\\btnBorrar.png"))
                BtnEditar.setIconSize(QtCore.QSize(28, 28))
                BtnBorrar.setIconSize(QtCore.QSize(28, 28))
                BtnEditar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                BtnBorrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                BtnEditar.clicked.connect(lambda: self.ventanaUsuarioEditar(usuario))
                BtnBorrar.clicked.connect(lambda: self.borrarUsuario(usuario))
               
        def editarUsuario(self):
                newUsuario = UsuarioModelo()
                newUsuario.setNombreU(self.loginAdmin.nameRegister.text())
                newUsuario.setContrasenaU(self.loginAdmin.codeRegister.text())
                if self.loginAdmin.adminCheck.isChecked():
                        typpe = 1
                else:
                        typpe = 2
                newUsuario.setRolU(typpe)
                self.loginAdmin.nameRegister.setText("")
                self.loginAdmin.codeRegister.setText("")
                self.usuarioC.actualizarUsuario(newUsuario, 5)
                self.loginAdmin.btnGuardar.hide()
                self.loginAdmin.registerButton.show()
                self.habilitarBtn(self.loginAdmin.registerButton)
                self.showUsers()
                self.ventanaUsuarioNormal()

        def ventanaUsuarioEditar(self, usuario):
                self.loginAdmin.frame_3.setStyleSheet("border-radius: 15px; \
                background-color: qlineargradient(spread:pad, x1:0.517, y1:0, \
                x2:0.506, y2:1, stop:0 rgba(251, 144, 8, 255), stop:1 rgba(255, 255, 255, 255));")
                self.loginAdmin.nameRegister.setText(f"{usuario[1]}")
                self.loginAdmin.label_2.setText("Editar Usuario")
                self.loginAdmin.label_2.setStyleSheet("color: white;")
                if usuario[2] == 'Administrador':
                        self.loginAdmin.adminCheck.setChecked(True)
                else:
                        self.loginAdmin.adminCheck.setChecked(False)
                self.loginAdmin.registerButton.hide()
                self.loginAdmin.btnGuardar.show()
        
        def ventanaUsuarioNormal(self):
                self.loginAdmin.frame_3.setStyleSheet("background-color: qlineargradient(spread:pad, \
                        x1:0.493, y1:0, x2:0.502, y2:1, stop:0 rgba(0, 166, 255, 255), stop:1 \
                        rgba(162, 254, 255, 0));\n""border-radius: 15px;\n""\n""\n""")
                self.loginAdmin.nameRegister.setText("")
                self.loginAdmin.nameRegister.setPlaceholderText("Nombre")
                self.loginAdmin.codeRegister.setText("")
                self.loginAdmin.codeRegister.setPlaceholderText("(4-6 carácteres)")
                self.loginAdmin.adminCheck.setChecked(False)
                self.loginAdmin.registerButton.show()
                self.loginAdmin.btnGuardar.hide()

        def borrarUsuario(self, usuario):
                reply = QtWidgets.QMessageBox.warning(self, "Atención", f"¿Está seguro que desea eliminar a {usuario[1]}?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
                if reply == QtWidgets.QMessageBox.Yes:
                        self.usuarioC.eliminarUsuario(usuario[0])
                        self.showUsers()
                        self.loginAdmin.userTable.removeRow(int(usuario[0])+1)
                else:
                        pass



                
