# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SITHome_Devices.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SITHome_Dispositivos(object):
    def setupUi(self, SITHome_Dispositivos):
        SITHome_Dispositivos.setObjectName("SITHome_Dispositivos")
        SITHome_Dispositivos.resize(1115, 717)
        SITHome_Dispositivos.setMinimumSize(QtCore.QSize(1115, 715))
        SITHome_Dispositivos.setMaximumSize(QtCore.QSize(1115, 717))
        SITHome_Dispositivos.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0.386364 rgba(162, 254, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(SITHome_Dispositivos)
        self.centralwidget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0.386364 rgba(162, 254, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"border-radius: 15px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.back = QtWidgets.QPushButton(self.frame)
        self.back.setMinimumSize(QtCore.QSize(80, 35))
        self.back.setMaximumSize(QtCore.QSize(80, 35))
        self.back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"border-radius: 15px;\n"
"font: 10pt;\n"
"color: white;")
        self.back.setObjectName("back")
        self.horizontalLayout_3.addWidget(self.back)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setMinimumSize(QtCore.QSize(80, 35))
        self.pushButton.setMaximumSize(QtCore.QSize(80, 35))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("background-color: white;\n"
"border-radius: 15px;\n"
"font: 10pt;")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.493, y1:0, x2:0.502, y2:1, stop:0 rgba(0, 166, 255, 255), stop:1 rgba(162, 254, 255, 0));\n"
"border-radius: 15px;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(7)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.frame_6)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.addDispositivo = QtWidgets.QPushButton(self.frame_6)
        self.addDispositivo.setMinimumSize(QtCore.QSize(40, 40))
        self.addDispositivo.setMaximumSize(QtCore.QSize(40, 40))
        self.addDispositivo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addDispositivo.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"border-radius: 15px;\n"
"font: 10pt;")
        self.addDispositivo.setObjectName("addDispositivo")
        self.horizontalLayout_2.addWidget(self.addDispositivo)
        self.verticalLayout_3.addWidget(self.frame_6)
        self.Dispositivos = QtWidgets.QTableWidget(self.frame_4)
        self.Dispositivos.setStyleSheet("background-color: white;")
        self.Dispositivos.setObjectName("Dispositivos")
        self.Dispositivos.setColumnCount(4)
        self.Dispositivos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Dispositivos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Dispositivos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Dispositivos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Dispositivos.setHorizontalHeaderItem(3, item)
        self.Dispositivos.horizontalHeader().setVisible(True)
        self.Dispositivos.horizontalHeader().setCascadingSectionResizes(False)
        self.Dispositivos.horizontalHeader().setDefaultSectionSize(115)
        self.Dispositivos.horizontalHeader().setHighlightSections(True)
        self.Dispositivos.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_3.addWidget(self.Dispositivos)
        self.gridLayout.addWidget(self.frame_4, 0, 1, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.493, y1:0, x2:0.502, y2:1, stop:0 rgba(0, 166, 255, 255), stop:1 rgba(162, 254, 255, 0));\n"
"border-radius: 15px;\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.addHabitacion = QtWidgets.QPushButton(self.frame_5)
        self.addHabitacion.setMinimumSize(QtCore.QSize(40, 40))
        self.addHabitacion.setMaximumSize(QtCore.QSize(40, 40))
        self.addHabitacion.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addHabitacion.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"border-radius: 15px;\n"
"font: 10pt;")
        self.addHabitacion.setObjectName("addHabitacion")
        self.horizontalLayout.addWidget(self.addHabitacion)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.tablaHabitaciones = QtWidgets.QTableWidget(self.frame_3)
        self.tablaHabitaciones.setMinimumSize(QtCore.QSize(0, 0))
        self.tablaHabitaciones.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tablaHabitaciones.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tablaHabitaciones.setStyleSheet("background-color: white;\n"
"")
        self.tablaHabitaciones.setObjectName("tablaHabitaciones")
        self.tablaHabitaciones.setColumnCount(3)
        self.tablaHabitaciones.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHabitaciones.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHabitaciones.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHabitaciones.setHorizontalHeaderItem(2, item)
        self.tablaHabitaciones.horizontalHeader().setDefaultSectionSize(150)
        self.verticalLayout_2.addWidget(self.tablaHabitaciones)
        self.gridLayout.addWidget(self.frame_3, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_2)
        SITHome_Dispositivos.setCentralWidget(self.centralwidget)

        self.retranslateUi(SITHome_Dispositivos)
        QtCore.QMetaObject.connectSlotsByName(SITHome_Dispositivos)

    def retranslateUi(self, SITHome_Dispositivos):
        _translate = QtCore.QCoreApplication.translate
        SITHome_Dispositivos.setWindowTitle(_translate("SITHome_Dispositivos", "MainWindow"))
        self.back.setText(_translate("SITHome_Dispositivos", "Salir"))
        self.label.setText(_translate("SITHome_Dispositivos", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; text-decoration: underline; color:#ffffff;\">SITHome-Dispositivos</span></p></body></html>"))
        self.pushButton.setText(_translate("SITHome_Dispositivos", "Usuarios"))
        self.label_3.setText(_translate("SITHome_Dispositivos", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ffffff;\">Dispositivos</span></p></body></html>"))
        self.addDispositivo.setText(_translate("SITHome_Dispositivos", "+"))
        item = self.Dispositivos.horizontalHeaderItem(0)
        item.setText(_translate("SITHome_Dispositivos", "Nombre"))
        item = self.Dispositivos.horizontalHeaderItem(1)
        item.setText(_translate("SITHome_Dispositivos", "Estado"))
        item = self.Dispositivos.horizontalHeaderItem(2)
        item.setText(_translate("SITHome_Dispositivos", "editar"))
        item = self.Dispositivos.horizontalHeaderItem(3)
        item.setText(_translate("SITHome_Dispositivos", "eliminar"))
        self.label_2.setText(_translate("SITHome_Dispositivos", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ffffff;\">Habitaciones</span></p></body></html>"))
        self.addHabitacion.setText(_translate("SITHome_Dispositivos", "+"))
        item = self.tablaHabitaciones.horizontalHeaderItem(0)
        item.setText(_translate("SITHome_Dispositivos", "Nombre"))
        item = self.tablaHabitaciones.horizontalHeaderItem(1)
        item.setText(_translate("SITHome_Dispositivos", "Editar"))
        item = self.tablaHabitaciones.horizontalHeaderItem(2)
        item.setText(_translate("SITHome_Dispositivos", "Eliminar"))
