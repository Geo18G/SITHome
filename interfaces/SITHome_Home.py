# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\SITHome_Home.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from assets import imagenes


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
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setStyleSheet("background-color: None;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Logo = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Logo.sizePolicy().hasHeightForWidth())
        self.Logo.setSizePolicy(sizePolicy)
        self.Logo.setMaximumSize(QtCore.QSize(320, 320))
        self.Logo.setStyleSheet("image: url(:/sin conexion/SITHome_Logo.png);\n"
"\n"
"background-color: None;\n"
"\n"
"")
        self.Logo.setText("")
        self.Logo.setScaledContents(True)
        self.Logo.setObjectName("Logo")
        self.horizontalLayout_2.addWidget(self.Logo)
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
        self.login.setGeometry(QtCore.QRect(490, 250, 111, 41))
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
        self.label_2.setGeometry(QtCore.QRect(500, 130, 81, 41))
        self.label_2.setStyleSheet("font: 24pt \"MS shell Dlg 2\";\n"
"background-color: none;\n"
"color: white;")
        self.label_2.setObjectName("label_2")
        self.loginCode_2 = QtWidgets.QLineEdit(self.frame_4)
        self.loginCode_2.setGeometry(QtCore.QRect(440, 60, 211, 41))
        self.loginCode_2.setStyleSheet("border-radius: 10px;\n"
"border: none;\n"
"font: 24px;\n"
"background-color: white;")
        self.loginCode_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.loginCode_2.setAlignment(QtCore.Qt.AlignCenter)
        self.loginCode_2.setObjectName("loginCode_2")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setGeometry(QtCore.QRect(470, 20, 141, 41))
        self.label_3.setStyleSheet("font: 24pt \"MS shell Dlg 2\";\n"
"background-color: none;\n"
"color: white;")
        self.label_3.setObjectName("label_3")
        self.nombre_Inc = QtWidgets.QLabel(self.frame_4)
        self.nombre_Inc.setGeometry(QtCore.QRect(450, 100, 201, 41))
        self.nombre_Inc.setStyleSheet("font: 24pt \"MS shell Dlg 2\";\n"
"background-color: none;\n"
"color: white;")
        self.nombre_Inc.setObjectName("nombre_Inc")
        self.contrasena_Inc = QtWidgets.QLabel(self.frame_4)
        self.contrasena_Inc.setGeometry(QtCore.QRect(470, 210, 151, 41))
        self.contrasena_Inc.setStyleSheet("font: 24pt \"MS shell Dlg 2\";\n"
"background-color: none;\n"
"color: white;")
        self.contrasena_Inc.setObjectName("contrasena_Inc")
        self.sin_Conex = QtWidgets.QLabel(self.frame_4)
        self.sin_Conex.setGeometry(QtCore.QRect(960, 20, 101, 71))
        self.sin_Conex.setStyleSheet("image: url(:/sin conexion/sin_conexion.png);\n"
"\n"
"background-color: rgb(255, 238, 47);")
        self.sin_Conex.setText("")
        self.sin_Conex.setObjectName("sin_Conex")
        self.horizontalLayout.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SITHome"))
        self.login.setText(_translate("MainWindow", "Ingresar"))
        self.login.setShortcut(_translate("MainWindow", "Return"))
        self.loginCode.setPlaceholderText(_translate("MainWindow", "******"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Contrase??a</span></p></body></html>"))
        self.loginCode_2.setPlaceholderText(_translate("MainWindow", "Usuario"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Nombre de usuario</span></p></body></html>"))
        self.nombre_Inc.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">Nombre de Usuario incorrecto</span></p></body></html>"))
        self.contrasena_Inc.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">Contrase??a incorrecta</span></p></body></html>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())