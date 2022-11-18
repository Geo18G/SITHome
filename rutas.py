from acciones import Acciones
import time

class Rutas(Acciones):
    def __init__(self):
        super(Rutas, self).__init__()
        self.asignarRutas()
        
    def asignarRutas(self):
        self.loginVista.home.home.login.clicked.connect(lambda: self.ingresar())
    
    
    def ingresar(self):
        ingreso = self.loginVista.SITHome_Login()
        if ingreso == True:
            print(1)
            self.loginVista.home.close()
            print(2)
            self.usuariosVista.usuarios.show()
            self.usuariosVista.showUsers()
            # self.usuariosVista.usuarios.show()
            print(3)
            pass
        else:
            self.loginVista.home.close()
            self.habitacionesVista.habitaciones.show()
            self.habitacionesVista.showRooms()
            print(2)
            pass
        
