from PyQt5.QtWidgets import *
# from Vistas.login_vista import LoginVista
import sys
from rutas import Rutas


if __name__=="__main__":
        app = QApplication([])  
        myapp = Rutas()
        myapp.loginVista.home.show()
        sys.exit(app.exec_())