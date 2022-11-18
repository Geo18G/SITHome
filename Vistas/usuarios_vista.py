from Controladores.usuarios_controlador import UsuarioControlador
from Controladores.habitaciones_controlador import HabitacionControlador
from Controladores.permisos_controlador import PermisosControlador
from Modelos.usuario_modelo import UsuarioModelo
from Modelos.permisos_modelo import PermisoModelo
# from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui, QtCore
# from interfaces.SITHome_LoginAdmin import Ui_MainWindow as Admin
from Vistas.habitaciones_vista import HabitacionesVista
import globales
from plantilla import Plantilla

class UsuariosVista(Plantilla):
        def __init__(self):
                super(UsuariosVista).__init__()
                self.usuarioC = UsuarioControlador()
                self.habitacionC = HabitacionControlador()
                self.permisosC = PermisosControlador()
                # self.inicialize()

        # def inicialize(self):
        #         #buttons-------------
        #         self.usuarios.usuarios.registerButton.clicked.connect(lambda: self.SITHome_register())
        #         self.usuarios.usuarios.viewPass.clicked.connect(lambda: self.viewPass())
        #         self.usuarios.usuarios.btnGuardar.clicked.connect(self.editarUsuario)
        #         self.usuarios.usuarios.addUser.clicked.connect(self.ventanaUsuarioNormal)
        #         self.usuarios.usuarios.dispButton.clicked.connect(self.goToHabitacionesVista)
        #         #elements & functions----------------
        #         self.usuarios.usuarios.registerButton.setEnabled(False)
        #         self.usuarios.usuarios.nameRegister.textChanged.connect(lambda: self.habilitarBtn(self.usuarios.usuarios.registerButton))
        #         self.usuarios.usuarios.codeRegister.textChanged.connect(lambda: self.habilitarBtn(self.usuarios.usuarios.registerButton))
        #         self.usuarios.usuarios.nameRegister.textChanged.connect(lambda: self.habilitarBtn(self.usuarios.usuarios.btnGuardar))
        #         self.usuarios.usuarios.codeRegister.textChanged.connect(lambda: self.habilitarBtn(self.usuarios.usuarios.btnGuardar))
        #         self.usuarios.usuarios.addUser.hide()
        #         self.usuarios.usuarios.btnGuardar.hide()

        def showUsers(self):
                self.usuarios.usuarios.userTable.clearContents()
                globales.Usuarios = self.usuarioC.mostrarUsuario()
                row = 0
                for user in globales.Usuarios:
                        column = 0
                        self.usuarios.usuarios.userTable.removeRow(row)
                        self.usuarios.usuarios.userTable.insertRow(row)
                        cell = QtWidgets.QTableWidgetItem(user[1])
                        self.usuarios.usuarios.userTable.setItem(row, column, cell)
                        column +=1
                        cell = QtWidgets.QTableWidgetItem(user[2])
                        self.usuarios.usuarios.userTable.setItem(row, column, cell)
                        self.agregarBtn(self.usuarios.usuarios.userTable, row, user)
                        row +=1
                        

        def SITHome_register(self):
                # globales.idHabitaciones = self.habitacionC.obtener_ids()
                newUsuario = UsuarioModelo()
                newUsuario.setNombreU(self.usuarios.usuarios.nameRegister.text())
                newUsuario.setContrasenaU(self.usuarios.usuarios.codeRegister.text())
                if self.usuarios.usuarios.adminCheck.isChecked():
                        typpe = 1
                else:
                        typpe = 2
                newUsuario.setRolU(typpe)
                retorno =  self.usuarioC.crearUsuario(newUsuario)
                if retorno == False:
                        self.usuarios.usuarios.nameRegister.setStyleSheet(
                                "border-radius: 10px; border: 2px solid red; font: 24px")
                        self.usuarios.usuarios.codeRegister.setStyleSheet(
                                "border-radius: 10px; border: 2px solid red; font: 24px")
                else:
                        self.usuarios.usuarios.nameRegister.setText("")
                        self.usuarios.usuarios.codeRegister.setText("")
                        self.showUsers()
                        self.habilitarBtn(self.usuarios.usuarios.registerButton)
                        for user in globales.Usuarios:
                                if user[1] == newUsuario.getNombreU():
                                        permiso = PermisoModelo()
                                        permiso.setIdUsuarioP(user[0])
                                        for hab in globales.Habitaciones:
                                                permiso.setIdHabitacionP(hab[0])
                                                if user[2] == "Administrador":
                                                        permiso.setPermiso(1)
                                                        self.permisosC.crearPermisos(permiso)
                                                else:
                                                        permiso.setPermiso(0)
                                                        self.permisosC.crearPermisos(permiso)







                # try:
                #         for hab in globales.idHabitaciones:
                #                 self.permisosC.nuevoUsuarioPermisos(newUsuario.getNombreU(), hab)
                #         print("permiso automatico agregado")
                # except:
                #         print("no se pudo agregar permiso automatico al usuario")

        def viewPass(self):
                self.usuarios.usuarios.codeRegister.setEchoMode(0)

        # def goToHabitacionesVista(self):
        #         goToHa = HabitacionesVista()
        #         self.usuarios.close()
        #         goToHa.habitaciones.show()
        #         goToHa.showRooms()


        def habilitarBtn(self, btn):
                if (len(self.usuarios.usuarios.codeRegister.text()) >=4 and len(self.usuarios.usuarios.nameRegister.text()) !=0):
                        btn.setEnabled(True)
                else:
                        btn.setEnabled(False)
        
        def agregarBtn(self, tabla, fila, usuario):
                BtnBorrar = QtWidgets.QPushButton()
                BtnEditar = QtWidgets.QPushButton()
                tabla.setCellWidget(fila, 2, BtnEditar)
                if int(usuario[0]) != int(globales.Usuario[0]):
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
                newUsuario.setNombreU(self.usuarios.usuarios.nameRegister.text())
                newUsuario.setContrasenaU(self.usuarios.usuarios.codeRegister.text())
                if self.usuarios.usuarios.adminCheck.isChecked():
                        typpe = 1
                else:
                        typpe = 2
                newUsuario.setRolU(typpe)
                self.usuarios.usuarios.nameRegister.setText("")
                self.usuarios.usuarios.codeRegister.setText("")
                usuariosRegistrados = self.usuarioC.mostrarUsuario()
                for usuario in usuariosRegistrados:
                        if usuario[1] == self.usuarios.usuarios.userTable.item(self.usuarios.usuarios.userTable.currentRow(), 0).text():
                                self.usuarioC.actualizarUsuario(newUsuario, usuario[0])
                self.usuarios.usuarios.btnGuardar.hide()
                self.usuarios.usuarios.registerButton.show()
                self.habilitarBtn(self.usuarios.usuarios.registerButton)
                self.showUsers()
                
                self.ventanaUsuarioNormal()

        def ventanaUsuarioEditar(self, usuario):
                self.usuarios.usuarios.frame_3.setStyleSheet("border-radius: 15px; \
                background-color: qlineargradient(spread:pad, x1:0.517, y1:0, \
                x2:0.506, y2:1, stop:0 rgba(251, 144, 8, 255), stop:1 rgba(255, 255, 255, 255));")
                self.usuarios.usuarios.nameRegister.setText(f"{usuario[1]}")
                self.usuarios.usuarios.label_2.setText("Editar Usuario")
                self.usuarios.usuarios.label_2.setStyleSheet("color: white;")
                if usuario[2] == 'Administrador':
                        self.usuarios.usuarios.adminCheck.setChecked(True)
                else:
                        self.usuarios.usuarios.adminCheck.setChecked(False)
                self.usuarios.usuarios.registerButton.hide()
                self.usuarios.usuarios.btnGuardar.show()
                self.usuarios.usuarios.addUser.show()

        def ventanaUsuarioNormal(self):
                self.usuarios.usuarios.label_2.setText("Agregar Nuevo Usuario")
                self.usuarios.usuarios.label_2.setStyleSheet("color: white;")
                self.usuarios.usuarios.frame_3.setStyleSheet("background-color: qlineargradient(spread:pad, \
                        x1:0.493, y1:0, x2:0.502, y2:1, stop:0 rgba(0, 166, 255, 255), stop:1 \
                        rgba(162, 254, 255, 0));\n""border-radius: 15px;\n""\n""\n""")
                self.usuarios.usuarios.nameRegister.setText("")
                self.usuarios.usuarios.nameRegister.setPlaceholderText("Nombre")
                self.usuarios.usuarios.codeRegister.setText("")
                self.usuarios.usuarios.codeRegister.setPlaceholderText("(4-6 carácteres)")
                self.usuarios.usuarios.adminCheck.setChecked(False)
                self.usuarios.usuarios.registerButton.show()
                self.usuarios.usuarios.btnGuardar.hide()
                self.usuarios.usuarios.addUser.hide()

        def borrarUsuario(self):
                # usuariosRegistrados = self.usuarioC.mostrarUsuario()
                for usuar in globales.Usuarios:
                        if usuar[1] == self.usuarios.usuarios.userTable.item(self.usuarios.usuarios.userTable.currentRow(), 0).text():
                                reply = QtWidgets.QMessageBox.warning(self, "Atención", f"¿Está seguro que desea eliminar a {usuar[1]}?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
                                if reply == QtWidgets.QMessageBox.Yes:
                                        self.permisosC.eliminarPermisosPorUs(usuar[0])
                                        self.usuarioC.eliminarUsuario(usuar[0])
                                        self.usuarios.usuarios.userTable.removeRow(self.usuarios.usuarios.userTable.currentRow())

                        else:
                                pass
                self.showUsers()



                
