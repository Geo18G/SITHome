from Controladores.habitaciones_controlador import HabitacionControlador
from Controladores.dispositivos_controlador import DispositivoControlador
from Modelos.habitacion_modelo import HabitacionModelo
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui, QtCore
from interfaces.SITHome_Devices import Ui_SITHome_Dispositivos as Habitaciones
from interfaces.SITHome_HabForm import Ui_Dialog as FormH
import globales

class Formulario(QDialog):
    def __init__(self):
        super(Formulario, self).__init__()
        self.uiForm  = FormH()
        self.uiForm.setupUi(self)

class HabitacionesUi(QMainWindow):
    def __init__(self):
        super(HabitacionesUi, self).__init__()
        self.habitaciones = Habitaciones()
        self.addH  = Formulario()
        self.habitaciones.setupUi(self)
        self.habitacionC = HabitacionControlador()
        self.dispositivosC = DispositivoControlador()
        self.inicialize()
        

    def inicialize(self):
        self.habitaciones.addHabitacion.clicked.connect(lambda: self.addH.show())
        self.addH.uiForm.btn_ok.clicked.connect(self.editarH)
       
        
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

    def showRooms(self):
        listaHabitaciones = list()
        for hab in globales.idHabitaciones:
            retorno = self.habitacionC.mostrarHabitacion(globales.Usuario[0],hab)
            if retorno != None:
                listaHabitaciones.append(retorno)
            else:
                pass
        row = 0
        column = 0
        self.habitaciones.tablaHabitaciones.removeRow(row)
        for hab in listaHabitaciones:
            self.habitaciones.tablaHabitaciones.insertRow(row)
            btnHabitacion = QtWidgets.QPushButton(text=f"{hab[1]}")
            btnHabitacion.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.habitaciones.tablaHabitaciones.setCellWidget(row, column, btnHabitacion)
            btnHabitacion.clicked.connect(lambda: self.showDevices())
            self.agregarBtn(self.habitaciones.tablaHabitaciones, row)
            row += 1
            
    
    def editarH(self):
        self.addH.show()  
        newHabitacion = HabitacionModelo()
        newHabitacion.setNombreH(self.addH.uiForm.nameRegister.text())
        listahab = list()
        for hab in globales.idHabitaciones:
            retorno = self.habitacionC.mostrarHabitacion(globales.Usuario[0], hab)
            if retorno != None:
                listahab.append(retorno)
                print(listahab)
        for x in listahab:
            if x[1] == self.habitaciones.tablaHabitaciones.cellWidget(self.habitaciones.tablaHabitaciones.currentRow(), 0).text():
                print("entra al if")
                self.habitacionC.actualizarHabitacion(newHabitacion, x[0])
        self.showRooms()
        self.addH.close()

    # def SITHome_register(self):
    #     newUsuario = UsuarioModelo()
    #     newUsuario.setNombreU(self.loginAdmin.nameRegister.text())
    #     newUsuario.setContrasenaU(self.loginAdmin.codeRegister.text())
    #     if self.loginAdmin.adminCheck.isChecked():
    #         typpe = 1
    #     else:
    #         typpe = 2
    #     newUsuario.setRolU(typpe)
    #     self.loginAdmin.nameRegister.setText("")
    #     self.loginAdmin.codeRegister.setText("")
    #     self.usuarioC.crearUsuario(newUsuario)
    #     self.showUsers()
    #     self.habilitarBtn()
    #
    # def viewPass(self):
    #     self.loginAdmin.codeRegister.setEchoMode(0)

    # def allDevs(self):
    #     UsuariosUi().hide()
    #     self.dispositivos.show()

    # def habilitarBtn(self):
    #     if (len(self.loginAdmin.codeRegister.text()) >= 4 and len(self.loginAdmin.nameRegister.text()) != 0):
    #         self.loginAdmin.registerButton.setEnabled(True)
    #     else:
    #         self.loginAdmin.registerButton.setEnabled(False)

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
        BtnEditar.clicked.connect(lambda: self.addH.show())
        
    def agregarBtnStatus(self, tabla, fila):
        BtnStatus = QtWidgets.QPushButton()
        tabla.setCellWidget(fila, 1, BtnStatus)
        BtnStatus.setMaximumSize(32, 32)
        BtnStatus.setIcon(QtGui.QIcon("assets\\interruptor-off.png"))
        BtnStatus.setIconSize(QtCore.QSize(32, 32))
        BtnStatus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        
        
    def addRoom(self):
        # self.addH.show()
        newHabitacion = HabitacionModelo()
        newHabitacion.setNombreH(self.addH.uiForm.nameRegister.text())
        self.habitacionC.crearHabitacion(newHabitacion)
    
    def mostrarAH(self):
        if globales.Usuario[3] != 1:
            self.habitaciones.addHabitacion.hide()
        else:
            pass
        
    def showDevices(self):
        
        print(self.habitaciones.tablaHabitaciones.cellWidget(self.habitaciones.tablaHabitaciones.currentRow(), 0).text())
        listaDispositivos = list()
        listaDispositivos = self.dispositivosC.mostrarDispositivos(1)
        # print(listaDispositivos)
        
        row = 0
        column = 0
        self.habitaciones.Dispositivos.removeRow(row)
        for dis in listaDispositivos:
            self.habitaciones.Dispositivos.insertRow(row)
            cell = QtWidgets.QTableWidgetItem(dis[0])
            self.habitaciones.Dispositivos.setItem(row, column, cell)
            self.agregarBtnStatus(self.habitaciones.Dispositivos, row)
            row += 1
            
    # self.habitaciones.tablaHabitaciones.cellWidget(self.habitaciones.tablaHabitaciones.currentRow(), 0).text()