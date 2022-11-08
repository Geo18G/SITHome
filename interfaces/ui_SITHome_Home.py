# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\cosas\SITHome\interfaces\SITHome_Home.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1115, 715)
        MainWindow.setMinimumSize(QtCore.QSize(1115, 715))
        MainWindow.setMaximumSize(QtCore.QSize(1115, 715))
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0.386364 rgba(162, 254, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: None;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setStyleSheet("font: 50pt  \"MS shell  Dlg 2\";\n"
"\n"
"background-color: None;\n"
"\n"
"")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setStyleSheet("background-color: None;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.493, y1:0, x2:0.502, y2:1, stop:0 rgba(0, 166, 255, 255), stop:1 rgba(162, 254, 255, 0));\n"
"border-radius: 15px;\n"
"")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.login = QtWidgets.QPushButton(self.frame_4)
        self.login.setGeometry(QtCore.QRect(490, 240, 111, 41))
        self.login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(0, 255, 0);\n"
"border: None;")
        self.login.setObjectName("login")
        self.loginCode = QtWidgets.QLineEdit(self.frame_4)
        self.loginCode.setGeometry(QtCore.QRect(450, 170, 191, 41))
        self.loginCode.setStyleSheet("border-radius: 10px;\n"
"border: none;\n"
"font: 24px;\n"
"background-color: white;")
        self.loginCode.setMaxLength(8)
        self.loginCode.setEchoMode(QtWidgets.QLineEdit.Password)
        self.loginCode.setAlignment(QtCore.Qt.AlignCenter)
        self.loginCode.setObjectName("loginCode")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setGeometry(QtCore.QRect(500, 130, 101, 41))
        self.label_2.setStyleSheet("font: 24pt \"MS shell Dlg 2\";\n"
"background-color: none;\n"
"color: white;")
        self.label_2.setObjectName("label_2")
        self.nombre = QtWidgets.QLineEdit(self.frame_4)
        self.nombre.setGeometry(QtCore.QRect(440, 60, 211, 41))
        self.nombre.setStyleSheet("border-radius: 10px;\n"
"border: none;\n"
"font: 24px;\n"
"background-color: white;")
        self.nombre.setMaxLength(6)
        self.nombre.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.nombre.setAlignment(QtCore.Qt.AlignCenter)
        self.nombre.setObjectName("nombre")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setGeometry(QtCore.QRect(460, 10, 181, 41))
        self.label_3.setStyleSheet("font: 24pt \"MS shell Dlg 2\";\n"
"background-color: none;\n"
"color: white;")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SITHome"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">SITHome</span></p></body></html>"))
        self.login.setText(_translate("MainWindow", "Ingresar"))
        self.login.setShortcut(_translate("MainWindow", "Return"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Contraseña</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Nombre de usuario</span></p></body></html>"))
