from Controladores.habitaciones_controlador import HabitacionControlador
from Controladores.dispositivos_controlador import DispositivoControlador
from Controladores.usuarios_controlador import UsuarioControlador
from Controladores.permisos_controlador import PermisosControlador
from Modelos.habitacion_modelo import HabitacionModelo
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui, QtCore
from interfaces.SITHome_Devices import Ui_SITHome_Dispositivos
from interfaces.SITHome_HabForm import Ui_Dialog
import globales

class Formulario(QDialog):
    def __init__(self):
        super(Formulario, self).__init__()
        self.uiForm = Ui_Dialog()
        self.uiForm.setupUi(self)


class HabitacionesUi(QMainWindow):
    def __init__(self):
        super(HabitacionesUi, self).__init__()
        self.habitaciones = Ui_SITHome_Dispositivos()
        self.addH  = Formulario()
        self.habitaciones.setupUi(self)
        self.habitacionC = HabitacionControlador()
        self.dispositivosC = DispositivoControlador()
        self.usuarioC = UsuarioControlador()
        self.permisosC = PermisosControlador()
        self.inicialize()
        

    def inicialize(self):
        self.habitaciones.addHabitacion.clicked.connect(lambda: self.mostrar_ventana_crear())
        self.addH.uiForm.btn_cancelar.clicked.connect(lambda: self.addH.close())
        self.addH.uiForm.btn_crear.setEnabled(False)
        self.addH.uiForm.btn_guardar.setEnabled(False)
        self.addH.uiForm.nameRegister.textChanged.connect(lambda: self.habilitarBtn(self.addH.uiForm.btn_crear))
        self.addH.uiForm.nameRegister.textChanged.connect(lambda: self.habilitarBtn(self.addH.uiForm.btn_guardar))
        self.addH.uiForm.btn_guardar.clicked.connect(lambda: self.editarH())
        self.addH.uiForm.btn_crear.clicked.connect(lambda: self.addRoom())

        # self.habitaciones.btn_salir.clicked.connect(lambda: self.salir_login())
        #self.addH.uiForm.btn_ok.clicked.connect(self.actualizarPermisos)
        # self.habitaciones.btn_usuarios.clicked.connect(lambda: self.usuarios_regresar())
    
        # self.showRooms()
        # self.habitaciones.registerButton.setEnabled(False)
        # self.habitaciones.registerButton.clicked.connect(lambda: self.SITHome_register())
        # self.habitaciones.viewPass.clicked.connect(lambda: self.viewPass())
        # self.habitaciones.dispButton.clicked.connect(lambda: UsuariosUi().allDevs())
        # self.habitaciones.nameRegister.textChanged.connect(self.habilitarBtn)
        # self.habitaciones.codeRegister.textChanged.connect(self.habilitarBtn)
        #
        # self.dispositivos.listaDispositivos.back.clicked.connect(lambda: self.dispositivos.hide())
        # self.dispositivos.listaDispositivos.back.clicked.connect(lambda: UsuariosUi().show())

    def mostrar_ventana_crear(self):
        self.addH.uiForm.nameRegister.setText("")
        self.addH.show()
        self.addH.uiForm.btn_guardar.hide()
        self.addH.uiForm.btn_crear.show()

    def mostrar_ventana_editar(self):
        self.addH.uiForm.nameRegister.setText(self.habitaciones.Habitaciones.cellWidget(self.habitaciones.Habitaciones.currentRow(), 0).text())
        for hab in globales.Habitaciones:
            if hab[1] == self.habitaciones.Habitaciones.cellWidget(self.habitaciones.Habitaciones.currentRow(), 0).text():
                self.mostrarUsuariosHab(hab[0])
        self.addH.show()
        self.addH.uiForm.btn_guardar.show()
        self.addH.uiForm.btn_crear.hide()

    def habilitarBtn(self, btn):
        if (len(self.addH.uiForm.nameRegister.text()) >= 4 and len(self.addH.uiForm.nameRegister.text()) != 0):
            btn.setEnabled(True)
        else:
            btn.setEnabled(False)

    def showRooms(self):
        globales.Habitaciones = self.habitacionC.obtener_Habitaciones()
        listaHabitaciones = []
        for hab in globales.Habitaciones:
            retorno = self.habitacionC.mostrarHabitacion(globales.Usuario[0],hab[0])
            if retorno != None:
                listaHabitaciones.append(retorno)
            else:
                pass
        self.mostrar_btnAH(globales.Usuario[2])
        self.habitaciones.Habitaciones.clearContents()
        row = 0
        column = 0
        for hab in listaHabitaciones:
            self.habitaciones.Habitaciones.removeRow(row)
            self.habitaciones.Habitaciones.insertRow(row)
            btnHabitacion = QtWidgets.QPushButton(text=f"{hab[1]}")
            btnHabitacion.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.habitaciones.Habitaciones.setCellWidget(row, column, btnHabitacion)
            btnHabitacion.clicked.connect(lambda: self.showDevices())
            if globales.Usuario[2] == "Administrador":
                self.agregarBtn(self.habitaciones.Habitaciones, row)
            row += 1


    def editarH(self):
        newHabitacion = HabitacionModelo()
        newHabitacion.setNombreH(self.addH.uiForm.nameRegister.text())
        for hab in globales.Habitaciones:
            if hab[1] == self.habitaciones.Habitaciones.cellWidget(self.habitaciones.Habitaciones.currentRow(), 0).text():
                self.habitacionC.actualizarHabitacion(newHabitacion,hab[0])
                self.actualizarPermisos(hab[0])
        self.addH.uiForm.nameRegister.setText("")
        self.addH.close()
        self.showRooms()

    def actualizarPermisos(self, habitacion):
        tabla = self.addH.uiForm.tableWidget
        for user in globales.Usuarios:
            if user[2] == 'Usuario':
                for row in range(tabla.rowCount()):
                    if tabla.item(row, 0).text() == user[1]:
                        if tabla.cellWidget(row, 1).isChecked():
                            self.permisosC.actualizarPermisos(user[0],habitacion, 1)
                            # print(f"permiso actualizado: SI para {user[1]} en habitación {habitacion}.")
                        else:
                            self.permisosC.actualizarPermisos(user[0],habitacion, 0)
                            # print(f"permiso actualizado: NO para {user[1]} en habitación {habitacion}.")

    def borrarH(self):
        for hab in globales.Habitaciones:
            if hab[1] == self.habitaciones.Habitaciones.cellWidget(self.habitaciones.Habitaciones.currentRow(), 0).text():
                reply = QtWidgets.QMessageBox.warning(self, "Atención",
                                                      f"¿Está seguro que desea eliminar la habitación con el nombre"
                                                      f" {hab[1]}?",
                                                      QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
                if reply == QtWidgets.QMessageBox.Yes:
                    # for usuario in globales.Usuarios:
                    self.permisosC.eliminarPermisosPorHab(hab[0])
                    self.habitacionC.eliminarHabitacion(hab[0])
                    self.habitaciones.Habitaciones.removeRow(self.habitaciones.Habitaciones.currentRow())
                    self.showRooms()


    def agregarBtn(self, tabla, fila):
        BtnBorrar = QtWidgets.QPushButton()
        BtnEditar = QtWidgets.QPushButton()
        tabla.setCellWidget(fila, 1, BtnEditar)
        tabla.setCellWidget(fila, 2, BtnBorrar)
        BtnEditar.setMaximumSize(32, 32)
        BtnBorrar.setMaximumSize(32, 32)
        BtnEditar.setIcon(QtGui.QIcon("assets\\btnEditar.png"))
        BtnBorrar.setIcon(QtGui.QIcon("assets\\btnBorrar.png"))
        BtnEditar.setIconSize(QtCore.QSize(32, 32))
        BtnBorrar.setIconSize(QtCore.QSize(32, 32))
        BtnEditar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        BtnBorrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        BtnEditar.clicked.connect(lambda: self.mostrar_ventana_editar())
        # BtnEditar.clicked.connect(self.mostrarUsuariosHab)
        BtnBorrar.clicked.connect(self.borrarH)

    def agregarBtnDis(self, tabla, fila, status):
        BtnBorrar = QtWidgets.QPushButton()
        BtnEditar = QtWidgets.QPushButton()
        BtnStatus = QtWidgets.QPushButton()
        tabla.setCellWidget(fila, 1, BtnStatus)
        tabla.setCellWidget(fila, 2, BtnEditar)
        tabla.setCellWidget(fila, 3, BtnBorrar)
        BtnEditar.setMaximumSize(32, 32)
        BtnBorrar.setMaximumSize(32, 32)
        BtnStatus.setMaximumSize(32, 32)
        if status == "1":
            BtnStatus.setIcon(QtGui.QIcon("assets\\interruptor-on.png"))
        else:
            BtnStatus.setIcon(QtGui.QIcon("assets\\interruptor-off.png"))
        BtnEditar.setIcon(QtGui.QIcon("assets\\btnEditar.png"))
        BtnBorrar.setIcon(QtGui.QIcon("assets\\btnBorrar.png"))
        BtnEditar.setIconSize(QtCore.QSize(32, 32))
        BtnBorrar.setIconSize(QtCore.QSize(32, 32))
        BtnStatus.setIconSize(QtCore.QSize(32, 32))
        BtnEditar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        BtnBorrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        BtnStatus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        
    # def agregarBtnStatus(self, tabla, fila):
    #     BtnStatus = QtWidgets.QPushButton()
    #     tabla.setCellWidget(fila, 1, BtnStatus)
    #     BtnStatus.setMaximumSize(32, 32)
    #     BtnStatus.setIcon(QtGui.QIcon("assets\\interruptor-off.png"))
    #     BtnStatus.setIconSize(QtCore.QSize(32, 32))
    #     BtnStatus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        
        
    def addRoom(self):
        newHabitacion = HabitacionModelo()
        newHabitacion.setNombreH(self.addH.uiForm.nameRegister.text())
        self.habitacionC.crearHabitacion(newHabitacion)
        self.addH.uiForm.nameRegister.setText("")
        self.addH.close()
        self.showRooms()

    
    def mostrar_btnAH(self,tipo):
        if tipo == "Administrador":
            self.habitaciones.addHabitacion.show()
        else:
            self.habitaciones.addHabitacion.hide()
        
        
    def showDevices(self):
        globales.Dispositivos = []
        for hab in globales.Habitaciones:
            if hab[1] == self.habitaciones.Habitaciones.cellWidget(self.habitaciones.Habitaciones.currentRow(), 0).text():
                globales.Dispositivos = self.dispositivosC.mostrarDispositivos(hab[0])
        self.habitaciones.Dispositivos.clearContents()
        row = 0
        for dis in globales.Dispositivos:
            column = 0
            self.habitaciones.Dispositivos.removeRow(row)
            self.habitaciones.Dispositivos.insertRow(row)
            cell = QtWidgets.QTableWidgetItem(dis[1])
            self.habitaciones.Dispositivos.setItem(row, column, cell)
            self.agregarBtnDis(self.habitaciones.Dispositivos, row, dis[2])
            row += 1


    def mostrarUsuariosHab(self,idH):
        tabla = self.addH.uiForm.tableWidget
        tabla.clearContents()
        # self.usuarioC.mostrarUsuario()
        row = 0
        for user in globales.Usuarios:
            tabla.removeRow(row)
            tabla.insertRow(row)
            cell = QtWidgets.QTableWidgetItem(user[1])
            tabla.setItem(row, 0, cell)
            self.agregarCheckBox(tabla, row, user, idH)
            row +=1

    def agregarCheckBox(self, tabla, fila, usuario, habitacion):
        check = QtWidgets.QCheckBox()
        permiso = self.permisosC.mostrarPermisos(usuario[0], habitacion)
        if permiso[0] == 1 and usuario[2] != "Administrador":
            check.setChecked(True)
            tabla.setCellWidget(fila, 1, check)
        if permiso[0] == 0 and usuario[2] != "Administrador":
            check.setChecked(False)
            tabla.setCellwidget(fila, 1, check)
        else:
            pass



    # def salir_login(self):
    #     self.close()
    #
    #     login = LoginVista()
    #     login.show()

    # def usuarios_regresar(self):
    #     self.close()
    #     main.myapp.show()





        
