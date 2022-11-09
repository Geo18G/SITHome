from Controladores.habitaciones_controlador import HabitacionControlador
from Modelos.habitacion_modelo import HabitacionModelo
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui, QtCore
from interfaces.SITHome_Devices import Ui_SITHome_Dispositivos as Habitaciones
import globales



class HabitacionesUi(QMainWindow):
    def __init__(self):
        super(HabitacionesUi, self).__init__()
        self.habitaciones = Habitaciones()
        self.habitaciones.setupUi(self)
        self.habitacionC = HabitacionControlador()
        self.inicialize()

    def inicialize(self):
        pass
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
        self.habitaciones.Habitaciones.clearContents()
        listaHabitaciones = list()
        for hab in globales.idHabitaciones:
            listaHabitaciones.append(self.habitacionC.mostrarHabitacion(globales.idUsuario,hab))
        print(listaHabitaciones)
        if listaHabitaciones[0][0] == None:
            pass
        else:
            row = 0
            for hab in listaHabitaciones:
                column = 0
                self.habitaciones.Habitaciones.removeRow(row)
                self.habitaciones.Habitaciones.insertRow(row)
                cell = QtWidgets.QTableWidgetItem(hab[1])
                self.habitaciones.Habitaciones.setItem(row, column, cell)
                column += 1
                # cell = QtWidgets.QTableWidgetItem(hab[2])
                self.habitaciones.Habitaciones.setItem(row, column, cell)
                self.agregarBtn(self.habitaciones.Habitaciones, row)
                row += 1

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
