from plantilla import Plantilla
from Controladores.dispositivos_controlador import DispositivoControlador
from Modelos.dispositivos_modelo import DispositivoModelo
import globales
from PyQt5 import QtWidgets, QtGui, QtCore


class DispositivoVista(Plantilla):
    def __init__(self):
        super(DispositivoVista, self).__init__()
        self.dispositivosC = DispositivoControlador()
        
    def editarD(self):
        newDevice = DispositivoModelo()
        newDevice.setNombreD(self.addD.uiFormD.nameRegister.text())
        newDevice.setStatusD(0)
        for hab in globales.Habitaciones:
            if hab[1] == self.addD.uiFormD.comboBoxH.currentText():
                newDevice.setHabitacionD(hab[0])
        for dis in globales.Dispositivos:
            if dis[1] == self.habitaciones.habitaciones.Dispositivos.item(self.habitaciones.habitaciones.Dispositivos.currentRow(), 0).text():
                self.dispositivosC.actualizarDispositivo(newDevice,dis[0])
        self.addD.uiFormD.nameRegister.setText("")
        self.addD.close()
        self.showDevices()

    def borrarD(self):
            elemento = self.habitaciones.habitaciones.Dispositivos.item(self.habitaciones.habitaciones.Dispositivos.currentRow(),
                                                                0).text()
            for dis in globales.Dispositivos:
                if dis[1] == elemento:
                    reply = QtWidgets.QMessageBox.warning(self.habitaciones, "Atención",
                                                        f"¿Está seguro que desea eliminar el dispositivo con el nombre"
                                                        f" {dis[1]}?",
                                                        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
                    if reply == QtWidgets.QMessageBox.Yes:
                        self.dispositivosC.eliminarDispositivo(dis[0])
                        self.habitaciones.habitaciones.Dispositivos.removeRow(self.habitaciones.habitaciones.Dispositivos.currentRow())
                self.showDevices()
                
    def agregarBtnDis(self, tabla, fila, id):
        BtnBorrar = QtWidgets.QPushButton()
        BtnEditar = QtWidgets.QPushButton()
        BtnStatus = QtWidgets.QPushButton()
        tabla.setCellWidget(fila, 1, BtnStatus)
        tabla.setCellWidget(fila, 2, BtnEditar)
        tabla.setCellWidget(fila, 3, BtnBorrar)
        BtnEditar.setMaximumSize(32, 32)
        BtnBorrar.setMaximumSize(32, 32)
        BtnStatus.setMaximumSize(32, 32)
        status=self.dispositivosC.obtenerStatus(id)
        print(status[0])
        if status[0] == 1:
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
        BtnBorrar.clicked.connect(lambda: self.borrarD())
        BtnEditar.clicked.connect(lambda: self.mostrar_ventana_editarD())
        
    def addDevice(self):
        newDevice = DispositivoModelo()
        newDevice.setNombreD(self.addD.uiFormD.nameRegister.text())
        newDevice.setStatusD(0)
        for hab in globales.Habitaciones:
            if hab[1] == self.addD.uiFormD.comboBoxH.currentText():
                newDevice.setHabitacionD(hab[0])
        retorno = self.dispositivosC.crearDispositivo(newDevice)
        print(retorno)
        if retorno == False:
            self.addD.uiFormD.dis_Exit.show()
            self.addD.uiFormD.nameRegister.setStyleSheet(
                "border-radius: 10px; border: 2px solid red; font: 24px")
            pass
        else:
            for hab in globales.Habitaciones:
                if hab[1] == self.addD.uiFormD.comboBoxH.currentText():
                    newDevice.setHabitacionD(hab[0])
            self.dispositivosC.crearDispositivo(newDevice)
            self.addD.uiFormD.nameRegister.setText("")
            self.addD.close()
        self.showDevices()

    def mostrar_ventana_crearD(self):
        self.addD.uiFormD.frame.setStyleSheet("background-color: qlineargradient(spread:pad, \
                                x1:0.493, y1:0, x2:0.502, y2:1, stop:0 rgba(0, 166, 255, 255), stop:1 \
                                rgba(162, 254, 255, 0));\n""border-radius: 15px;\n""\n""\n""")
        self.addD.uiFormD.label.setText("Agregar Nuevo Dispositivo ")
        self.addD.uiFormD.label.setStyleSheet("color: white; font: 28px;")
        self.addD.uiFormD.label.setAlignment(QtCore.Qt.AlignCenter)
        self.addD.uiFormD.comboBoxH.setCurrentIndex(0)
        self.addD.uiFormD.nameRegister.setText("")
        self.addD.show()
        self.addD.uiFormD.btn_guardar.hide()
        self.addD.uiFormD.btn_registrar.show()

    def mostrar_ventana_editarD(self):
        self.addD.uiFormD.frame.setStyleSheet("border-radius: 15px; \
                        background-color: qlineargradient(spread:pad, x1:0.517, y1:0, \
                        x2:0.506, y2:1, stop:0 rgba(251, 144, 8, 255), stop:1 rgba(255, 255, 255, 255));")
        self.addD.uiFormD.label.setText("Editar dispositivo")
        self.addD.uiFormD.label.setStyleSheet("color: white; font: 28px;")
        self.addD.uiFormD.label.setAlignment(QtCore.Qt.AlignCenter)
        self.addD.uiFormD.nameRegister.setText(self.habitaciones.habitaciones.Dispositivos.item(self.habitaciones.habitaciones.Dispositivos.currentRow(), 0).text())
        self.addD.show()
        self.addD.uiFormD.btn_guardar.show()
        self.addD.uiFormD.btn_registrar.hide()
        
    def showDevices(self):
        for i in range(0, globales.Contador):
            self.habitaciones.habitaciones.Dispositivos.removeRow(i)
        try:
            globales.Habitacion = self.habitaciones.habitaciones.Habitaciones.cellWidget(self.habitaciones.habitaciones.Habitaciones.currentRow(), 0).text()
            self.habitaciones.habitaciones.Dispositivos.clearContents()
            for hab in globales.Habitaciones:
                if hab[1] == globales.Habitacion:
                    globales.Dispositivos = self.dispositivosC.mostrarDispositivos(hab[0])

                globales.Contador = 0
                for dis in globales.Dispositivos:
                    column = 0
                    self.habitaciones.habitaciones.Dispositivos.removeRow(globales.Contador)
                    self.habitaciones.habitaciones.Dispositivos.insertRow(globales.Contador)
                    cell = QtWidgets.QTableWidgetItem(dis[1])
                    self.habitaciones.habitaciones.Dispositivos.setItem(globales.Contador, column, cell)
                    self.agregarBtnDis(self.habitaciones.habitaciones.Dispositivos,globales.Contador, dis[0])
                    globales.Contador += 1
        except:
            pass
        
    def changeStatus(self, idD, btn):
        estado = (self.dispositivosC.obtenerStatus(idD))
        if estado[0] == 0:
            self.dispositivosC.cambiarStatus(idD, 1)
            btn.setIcon(QtGui.QIcon("assets\\interruptor-on.png"))
        else:
            self.dispositivosC.cambiarStatus(idD, 0)
            btn.setIcon(QtGui.QIcon("assets\\interruptor-off.png"))
