# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\cosas\SITHome\interfaces\prueba_tabla.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.user_table = QtWidgets.QTableWidget(self.centralwidget)
        self.user_table.setGeometry(QtCore.QRect(60, 50, 461, 501))
        self.user_table.setStyleSheet("background-color: none;\n"
"border-radius: 15px;\n"
"")
        self.user_table.setGridStyle(QtCore.Qt.NoPen)
        self.user_table.setObjectName("user_table")
        self.user_table.setColumnCount(3)
        self.user_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.user_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.user_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.user_table.setHorizontalHeaderItem(2, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.user_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nombre"))
