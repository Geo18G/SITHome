# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SITHome_DispForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogD(object):
    def setupUi(self, DialogD):
        DialogD.setObjectName("DialogD")
        DialogD.resize(555, 320)
        DialogD.setMinimumSize(QtCore.QSize(555, 320))
        DialogD.setMaximumSize(QtCore.QSize(555, 320))
        DialogD.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0.386364 rgba(162, 254, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogD)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(DialogD)
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.493, y1:0, x2:0.502, y2:1, stop:0 rgba(0, 166, 255, 255), stop:1 rgba(162, 254, 255, 0));\n"
"border-radius: 15px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setStyleSheet("background: none;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setEnabled(True)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setStyleSheet("background: none;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 131, 41))
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.nameRegister = QtWidgets.QLineEdit(self.frame_3)
        self.nameRegister.setGeometry(QtCore.QRect(160, 10, 341, 41))
        self.nameRegister.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.nameRegister.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border : none;\n"
"font: 12pt;")
        self.nameRegister.setText("")
        self.nameRegister.setAlignment(QtCore.Qt.AlignCenter)
        self.nameRegister.setObjectName("nameRegister")
        self.comboBoxH = QtWidgets.QComboBox(self.frame_3)
        self.comboBoxH.setGeometry(QtCore.QRect(160, 60, 231, 22))
        self.comboBoxH.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border : none;\n"
"font: 12pt;")
        self.comboBoxH.setObjectName("comboBoxH")
        self.comboBoxH.addItem("")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 131, 41))
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setStyleSheet("background: none;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.btn_guardar = QtWidgets.QPushButton(self.frame_4)
        self.btn_guardar.setGeometry(QtCore.QRect(240, 30, 80, 35))
        self.btn_guardar.setMinimumSize(QtCore.QSize(80, 35))
        self.btn_guardar.setMaximumSize(QtCore.QSize(80, 35))
        self.btn_guardar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_guardar.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"border-radius: 15px;\n"
"font: 10pt;")
        self.btn_guardar.setObjectName("btn_guardar")
        self.btn_cancelar = QtWidgets.QPushButton(self.frame_4)
        self.btn_cancelar.setGeometry(QtCore.QRect(420, 30, 80, 35))
        self.btn_cancelar.setMinimumSize(QtCore.QSize(80, 35))
        self.btn_cancelar.setMaximumSize(QtCore.QSize(80, 35))
        self.btn_cancelar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cancelar.setStyleSheet("background-color: white;\n"
"border-radius: 15px;\n"
"font: 10pt;")
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.btn_registrar = QtWidgets.QPushButton(self.frame_4)
        self.btn_registrar.setGeometry(QtCore.QRect(330, 30, 80, 35))
        self.btn_registrar.setMinimumSize(QtCore.QSize(80, 35))
        self.btn_registrar.setMaximumSize(QtCore.QSize(80, 35))
        self.btn_registrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_registrar.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"border-radius: 15px;\n"
"font: 10pt;")
        self.btn_registrar.setObjectName("btn_registrar")
        self.dis_Exit = QtWidgets.QLabel(self.frame_4)
        self.dis_Exit.setEnabled(True)
        self.dis_Exit.setGeometry(QtCore.QRect(170, -10, 321, 31))
        self.dis_Exit.setStyleSheet("background-color: none;\n"
"color: white;")
        self.dis_Exit.setObjectName("dis_Exit")
        self.verticalLayout_3.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(DialogD)
        self.comboBoxH.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(DialogD)

    def retranslateUi(self, DialogD):
        _translate = QtCore.QCoreApplication.translate
        DialogD.setWindowTitle(_translate("DialogD", "SITHome-Formulario Dispositivo"))
        self.label.setText(_translate("DialogD", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; color:#ffffff;\">Agregar Nuevo Dispositivo</span></p></body></html>"))
        self.label_2.setText(_translate("DialogD", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">Nombre:</span></p></body></html>"))
        self.nameRegister.setPlaceholderText(_translate("DialogD", "\"Foco Inteligente\""))
        self.comboBoxH.setCurrentText(_translate("DialogD", "           --SELECCIONE--"))
        self.comboBoxH.setItemText(0, _translate("DialogD", "           --SELECCIONE--"))
        self.label_3.setText(_translate("DialogD", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">Habitación:</span></p></body></html>"))
        self.btn_guardar.setText(_translate("DialogD", "Guardar"))
        self.btn_cancelar.setText(_translate("DialogD", "Cancelar"))
        self.btn_registrar.setText(_translate("DialogD", "Registrar"))
        self.dis_Exit.setText(_translate("DialogD", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">El Nombre del Dispositivo ya Existe</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogD = QtWidgets.QDialog()
    ui = Ui_DialogD()
    ui.setupUi(DialogD)
    DialogD.show()
    sys.exit(app.exec_())
