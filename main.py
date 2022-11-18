from PyQt5.QtWidgets import *
import sys
from rutas import Rutas


if __name__=="__main__":
        app = QApplication([])  
        myapp = Rutas()
        myapp.loginVista.home.show()
        sys.exit(app.exec_())