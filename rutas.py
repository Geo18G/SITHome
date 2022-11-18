from acciones import Acciones
import time

class Rutas(Acciones):
    def __init__(self):
        super(Rutas, self).__init__()
        self.asignarRutas()
        
    def asignarRutas(self):
        self.loginVista.home.home.login.clicked.connect(self.ingresar)
        self.usuariosVista.usuarios.usuarios.dispButton.clicked.connect(lambda: self.ir_habitaciones(self.usuariosVista.usuarios))
        self.habitacionesVista.habitaciones.habitaciones.btn_usuarios.clicked.connect(lambda: self.ir_usuarios(self.habitacionesVista.habitaciones))
        self.habitacionesVista.habitaciones.habitaciones.btn_salir.clicked.connect(lambda: self.ir_login(self.habitacionesVista.habitaciones))


    def ingresar(self):
        ingreso = self.loginVista.SITHome_Login()
        if ingreso == True:
            self.ir_usuarios(self.loginVista.home)
        else:
            self.ir_habitaciones(self.loginVista.home)
        
    def ir_usuarios(self,de):
        de.close()
        self.usuariosVista.usuarios.show()
        self.usuariosVista.showUsers()
    
    def ir_login(self,de):
        de.close()
        self.loginVista.home.show()

    def ir_habitaciones(self, de):
        de.close()
        self.habitacionesVista.habitaciones.show()
        self.habitacionesVista.showRooms()

        
