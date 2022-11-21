from PyQt5.QtWidgets import *
import sys
from rutas import Rutas


if __name__=="__main__":
        app = QApplication([])  
        myapp = Rutas()
        myapp.loginVista.home.home.loginCode_2.setText("nacho")
        myapp.loginVista.home.home.loginCode.setText("1234")
        myapp.loginVista.home.show()
        sys.exit(app.exec_())