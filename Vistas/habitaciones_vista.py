from Controladores.habitaciones_controlador import HabitacionControlador
from Controladores.permisos_controlador import PermisosControlador
from Modelos.habitacion_modelo import HabitacionModelo
from Modelos.permisos_modelo import PermisoModelo
from Vistas.dispositivos_vista import *
from PyQt5 import QtWidgets, QtGui, QtCore
import globales


class HabitacionesVista(DispositivoVista):
    def __init__(self):
        super(HabitacionesVista, self).__init__()
        self.habitacionC = HabitacionControlador()
        self.permisosC = PermisosControlador()


    def mostrar_ventana_crear(self):
        self.addH.uiForm.frame.setStyleSheet("background-color: qlineargradient(spread:pad, \
                        x1:0.493, y1:0, x2:0.502, y2:1, stop:0 rgba(0, 166, 255, 255), stop:1 \
                        rgba(162, 254, 255, 0));\n""border-radius: 15px;\n""\n""\n""")
        self.addH.uiForm.nombreHab.setText("Agregar Habitación")
        self.addH.uiForm.nombreHab.setStyleSheet("color: white; font: 28px;")
        self.addH.uiForm.nombreHab.setAlignment(QtCore.Qt.AlignCenter)
        self.addH.uiForm.nameRegister.setText("")
        self.mostrarUsuariosHab(None, "crear")
        self.addH.show()
        self.addH.uiForm.btn_guardar.hide()
        self.addH.uiForm.btn_crear.show()

    def mostrar_ventana_editar(self):
        self.addH.uiForm.frame.setStyleSheet("border-radius: 15px; \
                background-color: qlineargradient(spread:pad, x1:0.517, y1:0, \
                x2:0.506, y2:1, stop:0 rgba(251, 144, 8, 255), stop:1 rgba(255, 255, 255, 255));")
        self.addH.uiForm.nombreHab.setText("Editar Habitación")
        self.addH.uiForm.nombreHab.setStyleSheet("color: white; font: 28px;")
        self.addH.uiForm.nombreHab.setAlignment(QtCore.Qt.AlignCenter)
        self.addH.uiForm.nameRegister.setText(self.habitaciones.habitaciones.Habitaciones.cellWidget(self.habitaciones.habitaciones.Habitaciones.currentRow(), 0).text())
        for hab in globales.Habitaciones:
            if hab[1] == self.habitaciones.habitaciones.Habitaciones.cellWidget(self.habitaciones.habitaciones.Habitaciones.currentRow(), 0).text():
                self.mostrarUsuariosHab(hab[0], "editar")
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
        self.habitaciones.habitaciones.Habitaciones.clearContents()

        row = 0
        for hab in listaHabitaciones:
            self.habitaciones.habitaciones.Habitaciones.removeRow(row)
            self.habitaciones.habitaciones.Habitaciones.insertRow(row)
            botonHabitacion = self.crearBotonHab(hab[1])
            self.habitaciones.habitaciones.Habitaciones.setCellWidget(row, 0, botonHabitacion)
            if globales.Usuario[2] == "Administrador":
                self.agregarBtn(self.habitaciones.habitaciones.Habitaciones, row)
            row += 1
            self.addD.uiFormD.comboBoxH.addItem(hab[1])
            
    def crearBotonHab(self,hab):
        btnHabitacion = QtWidgets.QPushButton(text=f"{hab}")
        btnHabitacion.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        btnHabitacion.setStyleSheet("border-radius: 18px;border: 8px solid white;color: white;font: 12px black; background-color: rgb(0, 170, 255)")
        btnHabitacion.clicked.connect(self.showDevices)
        btnHabitacion.clicked.connect(self.showDevices)
        return btnHabitacion
        


    def editarH(self):
        newRoom = HabitacionModelo()
        newRoom.setNombreH(self.addH.uiForm.nameRegister.text())
        for hab in globales.Habitaciones:
            if hab[1] == self.habitaciones.habitaciones.Habitaciones.cellWidget(self.habitaciones.habitaciones.Habitaciones.currentRow(), 0).text():
                self.habitacionC.actualizarHabitacion(newRoom,hab[0])
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
                        else:
                            self.permisosC.actualizarPermisos(user[0],habitacion, 0)

    def borrarH(self):
        for hab in globales.Habitaciones:
            if hab[1] == self.habitaciones.habitaciones.Habitaciones.cellWidget(self.habitaciones.habitaciones.Habitaciones.currentRow(), 0).text():
                reply = QtWidgets.QMessageBox.warning(self.habitaciones, "Atención",
                                                      f"¿Está seguro que desea eliminar la habitación con el nombre"
                                                      f" {hab[1]}?",
                                                      QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
                if reply == QtWidgets.QMessageBox.Yes:
                    self.permisosC.eliminarPermisosPorHab(hab[0])
                    self.dispositivosC.eliminarDispositivosPorHab(hab[0])
                    self.habitacionC.eliminarHabitacion(hab[0])
                    self.habitaciones.habitaciones.Habitaciones.removeRow(self.habitaciones.habitaciones.Habitaciones.currentRow())
                    self.showRooms()
                    return True

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
        BtnEditar.clicked.connect(self.mostrar_ventana_editar)
        BtnBorrar.clicked.connect(self.borrarH)

    def addRoom(self):
        newRoom = HabitacionModelo()
        newRoom.setNombreH(self.addH.uiForm.nameRegister.text())
        retorno = self.habitacionC.crearHabitacion(newRoom)
        if retorno == False:
            self.addH.uiForm.hab_Exit.show()
            self.addH.uiForm.nameRegister.setStyleSheet(
                "border-radius: 10px; border: 2px solid red; font: 24px")
        else:
            self.addH.uiForm.nameRegister.setText("")
            self.addH.close()
            globales.Habitaciones = self.habitacionC.obtener_Habitaciones()
            for hab in globales.Habitaciones:
                if hab[1] == newRoom.getNombreH():
                    permiso = PermisoModelo()
                    permiso.setIdHabitacionP(hab[0])
                    for user in globales.Usuarios:
                        permiso.setIdUsuarioP(user[0])
                        if user[2] == "Administrador":
                            permiso.setPermiso(1)
                            self.permisosC.crearPermisos(permiso)
                        else:
                            permiso.setPermiso(0)
                            self.permisosC.crearPermisos(permiso)
            self.showRooms()

    def mostrar_btnAH(self,tipo):
        if tipo == "Administrador":
            self.habitaciones.habitaciones.addHabitacion.show()
        else:
            self.habitaciones.habitaciones.addHabitacion.hide()


    def mostrarUsuariosHab(self,idH, caso):
        tabla = self.addH.uiForm.tableWidget
        tabla.clearContents()
        row = 0
        for user in globales.Usuarios:
            tabla.removeRow(row)
            tabla.insertRow(row)
            cell = QtWidgets.QTableWidgetItem(user[1])
            tabla.setItem(row, 0, cell)
            self.agregarCheckBox(tabla, row, user, idH, caso)
            row +=1

    def agregarCheckBox(self, tabla, fila, usuario, habitacion, caso):
        check = QtWidgets.QCheckBox()
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


    





        
