# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\SITHome_LoginAdmin.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1124, 716)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0.386364 rgba(162, 254, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.493, y1:0, x2:0.502, y2:1, stop:0 rgba(0, 166, 255, 255), stop:1 rgba(162, 254, 255, 0));\n"
"border-radius: 15px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 20, 451, 71))
        self.label.setStyleSheet("border: 3px solid black;\n"
"font : black;")
        self.label.setObjectName("label")
        self.userTable = QtWidgets.QTableWidget(self.frame)
        self.userTable.setGeometry(QtCore.QRect(20, 180, 461, 501))
        self.userTable.setStyleSheet("background-color: none;\n"
"border-radius: 15px;")
        self.userTable.setGridStyle(QtCore.Qt.NoPen)
        self.userTable.setObjectName("userTable")
        self.userTable.setColumnCount(2)
        self.userTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.userTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.userTable.setHorizontalHeaderItem(1, item)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(150, 120, 211, 31))
        self.label_5.setStyleSheet("background-color: none;")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setStyleSheet("background-color: None;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setMinimumSize(QtCore.QSize(500, 320))
        self.frame_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.493, y1:0, x2:0.502, y2:1, stop:0 rgba(0, 166, 255, 255), stop:1 rgba(162, 254, 255, 0));\n"
"border-radius: 15px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_4.setStyleSheet("background-color: None;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setTabletTracking(False)
        self.frame_6.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.frame_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_6.setAutoFillBackground(False)
        self.frame_6.setStyleSheet("background-color: None;")
        self.frame_6.setInputMethodHints(QtCore.Qt.ImhPreferUppercase)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_3 = QtWidgets.QLabel(self.frame_6)
        self.label_3.setGeometry(QtCore.QRect(30, 20, 101, 41))
        self.label_3.setStyleSheet("background-color: None;")
        self.label_3.setObjectName("label_3")
        self.nameRegister = QtWidgets.QLineEdit(self.frame_6)
        self.nameRegister.setGeometry(QtCore.QRect(140, 20, 341, 41))
        self.nameRegister.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border : none;\n"
"font: 12pt;")
        self.nameRegister.setAlignment(QtCore.Qt.AlignCenter)
        self.nameRegister.setObjectName("nameRegister")
        self.verticalLayout_2.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.frame_3)
        self.frame_7.setStyleSheet("background-color: None;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_4 = QtWidgets.QLabel(self.frame_7)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 101, 41))
        self.label_4.setStyleSheet("background-color: None;")
        self.label_4.setObjectName("label_4")
        self.codeRegister = QtWidgets.QLineEdit(self.frame_7)
        self.codeRegister.setGeometry(QtCore.QRect(100, 20, 301, 41))
        self.codeRegister.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.codeRegister.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border : none;\n"
"font: 12pt;")
        self.codeRegister.setText("")
        self.codeRegister.setMaxLength(6)
        self.codeRegister.setFrame(False)
        self.codeRegister.setEchoMode(QtWidgets.QLineEdit.Password)
        self.codeRegister.setAlignment(QtCore.Qt.AlignCenter)
        self.codeRegister.setObjectName("codeRegister")
        self.viewPass = QtWidgets.QPushButton(self.frame_7)
        self.viewPass.setGeometry(QtCore.QRect(430, 20, 41, 41))
        self.viewPass.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.viewPass.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border : 1px solid gray;")
        self.viewPass.setObjectName("viewPass")
        self.verticalLayout_2.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_3)
        self.frame_8.setStyleSheet("background-color: None;")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.adminCheck = QtWidgets.QCheckBox(self.frame_8)
        self.adminCheck.setGeometry(QtCore.QRect(10, 20, 151, 41))
        self.adminCheck.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.adminCheck.setStyleSheet("font: 12pt;\n"
"background-color: None;")
        self.adminCheck.setIconSize(QtCore.QSize(30, 30))
        self.adminCheck.setTristate(False)
        self.adminCheck.setObjectName("adminCheck")
        self.registerButton = QtWidgets.QPushButton(self.frame_8)
        self.registerButton.setGeometry(QtCore.QRect(330, 10, 111, 51))
        self.registerButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.registerButton.setStyleSheet("background-color: rgb(82, 255, 56);\n"
"border-radius: 15px;\n"
"border : none;\n"
"font: 11pt;")
        self.registerButton.setObjectName("registerButton")
        self.verticalLayout_2.addWidget(self.frame_8)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.frame_5.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.493, y1:0, x2:0.502, y2:1, stop:0 rgba(0, 166, 255, 255), stop:1 rgba(162, 254, 255, 0));\n"
"border-radius: 15px;\n"
"")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_9 = QtWidgets.QFrame(self.frame_5)
        self.frame_9.setStyleSheet("background-color: None;")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.frame_9)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.verticalLayout_4.addWidget(self.frame_9)
        self.frame_10 = QtWidgets.QFrame(self.frame_5)
        self.frame_10.setStyleSheet("background-color: None;\n"
"")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.dispButton = QtWidgets.QPushButton(self.frame_10)
        self.dispButton.setGeometry(QtCore.QRect(160, 40, 161, 61))
        self.dispButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dispButton.setStyleSheet("border-radius: 15px;\n"
"background-color: qlineargradient(spread:pad, x1:0.497975, y1:0, x2:0.502, y2:1, stop:0.736318 rgba(255, 255, 255, 255), stop:1 rgba(192, 255, 255, 255));")
        self.dispButton.setObjectName("dispButton")
        self.verticalLayout_4.addWidget(self.frame_10)
        self.verticalLayout.addWidget(self.frame_5)
        self.horizontalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#000000;\">SITHome Administrador</span></p></body></html>"))
        item = self.userTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.userTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tipo"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Usuarios Registrados</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Agregar nuevo usuario</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Nombre:</span></p></body></html>"))
        self.nameRegister.setPlaceholderText(_translate("MainWindow", "Nombre"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Código:</span></p></body></html>"))
        self.codeRegister.setPlaceholderText(_translate("MainWindow", "(Máximo 6 carácteres) "))
        self.viewPass.setText(_translate("MainWindow", "ver"))
        self.adminCheck.setText(_translate("MainWindow", "Administrador"))
        self.registerButton.setText(_translate("MainWindow", "Registrar"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Administrar Dispositivos</span></p></body></html>"))
        self.dispButton.setText(_translate("MainWindow", "Entrar"))
