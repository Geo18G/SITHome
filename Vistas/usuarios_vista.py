from Controladores.usuarios_controlador import UsuarioControlador
from Modelos.usuario_modelo import UsuarioModelo
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui, QtCore
from interfaces.SITHome_LoginAdmin import Ui_MainWindow as Admin
from Vistas.habitaciones_vista import HabitacionesUi
import globales

class UsuariosUi(QMainWindow):
        def __init__(self):
                super(UsuariosUi, self).__init__()
                self.loginAdmin = Admin()
                self.loginAdmin.setupUi(self)
                self.habitaciones = HabitacionesUi()
                self.usuarioC = UsuarioControlador()
                self.inicialize()

        def inicialize(self):
                #buttons-------------
                self.loginAdmin.registerButton.clicked.connect(lambda: self.SITHome_register())
                self.loginAdmin.viewPass.clicked.connect(lambda: self.viewPass())
                self.loginAdmin.btnGuardar.clicked.connect(self.editarUsuario)
                self.loginAdmin.addUser.clicked.connect(self.ventanaUsuarioNormal)
                self.loginAdmin.dispButton.clicked.connect(self.goToHabitacionesVista)
                #elements & functions----------------
                self.loginAdmin.registerButton.setEnabled(False)
                self.loginAdmin.nameRegister.textChanged.connect(lambda: self.habilitarBtn(self.loginAdmin.registerButton))
                self.loginAdmin.codeRegister.textChanged.connect(lambda: self.habilitarBtn(self.loginAdmin.registerButton))
                self.loginAdmin.nameRegister.textChanged.connect(lambda: self.habilitarBtn(self.loginAdmin.btnGuardar))
                self.loginAdmin.codeRegister.textChanged.connect(lambda: self.habilitarBtn(self.loginAdmin.btnGuardar))
                self.loginAdmin.addUser.hide()
                self.loginAdmin.btnGuardar.hide()

        def showUsers(self):
                self.ocultar_btn_borrar()
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

        def goToHabitacionesVista(self):
                self.close()
                self.habitaciones.show()
                self.habitaciones.showRooms()


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
                BtnBorrar.clicked.connect(lambda: self.borrarUsuario())

        def ocultar_btn_borrar(self):
                pass
               
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
                usuariosRegistrados = self.usuarioC.mostrarUsuario()
                for usuario in usuariosRegistrados:
                        if usuario[1] == self.loginAdmin.userTable.item(self.loginAdmin.userTable.currentRow(), 0).text():
                                self.usuarioC.actualizarUsuario(newUsuario, usuario[0])
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
                self.loginAdmin.addUser.show()

        def ventanaUsuarioNormal(self):
                self.loginAdmin.label_2.setText("Agregar Nuevo Usuario")
                self.loginAdmin.label_2.setStyleSheet("color: white;")
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
                self.loginAdmin.addUser.hide()

        def borrarUsuario(self):
                usuariosRegistrados = self.usuarioC.mostrarUsuario()
                for usuar in usuariosRegistrados:
                        if usuar[1] == self.loginAdmin.userTable.item(self.loginAdmin.userTable.currentRow(), 0).text():
                                reply = QtWidgets.QMessageBox.warning(self, "Atención", f"¿Está seguro que desea eliminar a {usuar[1]}?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
                                if reply == QtWidgets.QMessageBox.Yes:
                                        self.usuarioC.eliminarUsuario(usuar[0])
                                        self.loginAdmin.userTable.removeRow(self.loginAdmin.userTable.currentRow())
                                        self.showUsers()
                        else:
                                pass



                
