from Controladores.habitaciones_controlador import HabitacionControlador
from Controladores.dispositivos_controlador import DispositivoControlador
from Controladores.usuarios_controlador import UsuarioControlador
from Controladores.permisos_controlador import PermisosControlador
from Modelos.habitacion_modelo import HabitacionModelo
from Modelos.dispositivos_modelo import DispositivoModelo
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui, QtCore
from interfaces.SITHome_Devices import Ui_SITHome_Dispositivos
from interfaces.SITHome_HabForm import Ui_Dialog
from interfaces.SITHome_DispForm import Ui_DialogD
import globales

class FormularioH(QDialog):
    def __init__(self):
        super(FormularioH, self).__init__()
        self.uiForm = Ui_Dialog()
        self.uiForm.setupUi(self)

class FormularioD(QDialog):
    def __init__(self):
        super(FormularioD, self).__init__()
        self.uiFormD = Ui_DialogD()
        self.uiFormD.setupUi(self)


class HabitacionesUi(QMainWindow):
    def __init__(self):
        super(HabitacionesUi, self).__init__()
        self.habitaciones = Ui_SITHome_Dispositivos()
        self.addH = FormularioH()
        self.addD = FormularioD()
        self.habitaciones.setupUi(self)
        self.habitacionC = HabitacionControlador()
        self.dispositivosC = DispositivoControlador()
        self.usuarioC = UsuarioControlador()
        self.permisosC = PermisosControlador()
        self.inicialize()
        

    def inicialize(self):
        self.habitaciones.addHabitacion.clicked.connect(lambda: self.mostrar_ventana_crear())
        self.addH.uiForm.btn_cancelar.clicked.connect(lambda: self.addH.close())
        self.addD.uiFormD.btn_cancelar.clicked.connect(lambda: self.addD.close())
        self.addH.uiForm.btn_crear.setEnabled(False)
        self.addH.uiForm.btn_guardar.setEnabled(False)
        self.addD.uiFormD.btn_registrar.setEnabled(False)
        self.addD.uiFormD.btn_guardar.setEnabled(False)
        self.addH.uiForm.nameRegister.textChanged.connect(lambda: self.habilitarBtn(self.addH.uiForm.btn_crear, self.addH.uiForm.nameRegister))
        self.addH.uiForm.nameRegister.textChanged.connect(lambda: self.habilitarBtn(self.addH.uiForm.btn_guardar, self.addH.uiForm.nameRegister))
        self.addD.uiFormD.nameRegister.textChanged.connect(lambda: self.habilitarBtn(self.addD.uiFormD.btn_registrar, self.addD.uiFormD.nameRegister))
        self.addD.uiFormD.nameRegister.textChanged.connect(lambda: self.habilitarBtn(self.addD.uiFormD.btn_guardar, self.addD.uiFormD.nameRegister))
        self.addH.uiForm.btn_guardar.clicked.connect(lambda: self.editarH())
        self.addH.uiForm.btn_crear.clicked.connect(lambda: self.addRoom())
        self.addD.uiFormD.btn_registrar.clicked.connect(lambda: self.addDevice())
        self.habitaciones.addDispositivo.clicked.connect(lambda: self.mostrar_ventana_crearD())
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

        # self.mostrarUsuariosHab(hab[0])
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

    def habilitarBtn(self, btn, form):
        if len(form.text()) >= 4 and len(form.text()) != 0:
            btn.setEnabled(True)
        else:
            btn.setEnabled(False)

    def showRooms(self):
        globales.Habitaciones = self.habitacionC.obtener_Habitaciones()
        self.addD.uiFormD.comboBoxH.clear()
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
            self.addD.uiFormD.comboBoxH.addItem(hab[1])


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

    def agregarBtnDis(self, tabla, fila, status, id):
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
        BtnStatus.clicked.connect(lambda: self.changeStatus(id, BtnStatus))

        
    # def agregarBtnStatus(self, tabla, fila):
    #     BtnStatus = QtWidgets.QPushButton()
    #     tabla.setCellWidget(fila, 1, BtnStatus)
    #     BtnStatus.setMaximumSize(32, 32)
    #     BtnStatus.setIcon(QtGui.QIcon("assets\\interruptor-off.png"))
    #     BtnStatus.setIconSize(QtCore.QSize(32, 32))
    #     BtnStatus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        
        
    def addRoom(self):
        newRoom = HabitacionModelo()
        newRoom.setNombreH(self.addH.uiForm.nameRegister.text())
        self.habitacionC.crearHabitacion(newRoom)
        self.addH.uiForm.nameRegister.setText("")
        self.addH.close()
        self.showRooms()

    def addDevice(self):
        newDevice = DispositivoModelo()
        newDevice.setNombreD(self.addD.uiFormD.nameRegister.text())
        newDevice.setStatusD(0)
        for hab in globales.Habitaciones:
            if hab[1] == self.addD.uiFormD.comboBoxH.currentText():
                newDevice.setHabitacionD(hab[0])
        self.dispositivosC.crearDispositivo(newDevice)
        self.addD.uiFormD.nameRegister.setText("")
        self.addD.close()
        self.showDevices()

    def mostrar_ventana_crearD(self):
        self.addD.uiFormD.comboBoxH.setCurrentIndex(0)
        self.addD.uiFormD.nameRegister.setText("")
        self.addD.show()
        self.addD.uiFormD.btn_guardar.hide()
        self.addD.uiFormD.btn_registrar.show()

    
    def mostrar_btnAH(self,tipo):
        if tipo == "Administrador":
            self.habitaciones.addHabitacion.show()
        else:
            self.habitaciones.addHabitacion.hide()
        
        
    def showDevices(self):
        # globales.Dispositivos = []
        for hab in globales.Habitaciones:
            if hab[1] == self.habitaciones.Habitaciones.cellWidget(self.habitaciones.Habitaciones.currentRow(), 0).text():
                globales.Dispositivos = self.dispositivosC.mostrarDispositivos(hab[0])
        for row in range(self.habitaciones.Dispositivos.rowCount()):
            self.habitaciones.Dispositivos.removeRow(row)
        row = 0
        for dis in globales.Dispositivos:
            column = 0
            self.habitaciones.Dispositivos.removeRow(row)
            self.habitaciones.Dispositivos.insertRow(row)
            cell = QtWidgets.QTableWidgetItem(dis[1])
            self.habitaciones.Dispositivos.setItem(row, column, cell)
            self.agregarBtnDis(self.habitaciones.Dispositivos, row, dis[2], dis[0])
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

    def agregarCheckBox(self, tabla, fila, usuario, habitacion, caso):
        check = QtWidgets.QCheckBox()
        # print(tabla,fila,usuario,habitacion)
        permiso = self.permisosC.mostrarPermisos(usuario[0], habitacion)
        if caso == "editar":
            if usuario[2] == "Usuario":
                tabla.setCellWidget(fila, 1, check)
                if permiso[0] == 1:
                    check.setChecked(True)
                elif permiso[0] == 0:
                    check.setChecked(False)
            else:
                pass
        else:
            if usuario[2] == "Usuario":
                tabla.setCellWidget(fila, 1, check)
            else:
                pass

    def changeStatus(self, idD, btn):
        estado = (self.dispositivosC.obtenerStatus(idD))
        if estado[0] == 0:
            self.dispositivosC.cambiarStatus(idD, 1)
            btn.setIcon(QtGui.QIcon("assets\\interruptor-on.png"))
        else:
            self.dispositivosC.cambiarStatus(idD, 0)
            btn.setIcon(QtGui.QIcon("assets\\interruptor-off.png"))

    
    # def salir_login(self):
    #     self.close()
    #
    #     login = LoginVista()
    #     login.show()

    # def usuarios_regresar(self):
    #     self.close()
    #     main.myapp.show()





        
