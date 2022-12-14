import globales
from acciones import Acciones


class Rutas(Acciones):
    def __init__(self):
        super(Rutas, self).__init__()
        self.asignarRutas()
        
    def asignarRutas(self):
        self.loginVista.home.home.login.clicked.connect(self.ingresar)
        self.usuariosVista.usuarios.usuarios.btn_irHab.clicked.connect(lambda: self.ir_habitaciones(self.usuariosVista.usuarios))
        self.habitacionesVista.habitaciones.habitaciones.btn_usuarios.clicked.connect(lambda: self.ir_usuarios(self.habitacionesVista.habitaciones))
        self.habitacionesVista.habitaciones.habitaciones.btn_salir.clicked.connect(lambda: self.ir_login(self.habitacionesVista.habitaciones))
        self.usuariosVista.usuarios.usuarios.btn_Salir.clicked.connect(lambda: self.ir_login(self.usuariosVista.usuarios))


    def ingresar(self):
        ingreso = self.loginVista.SITHome_Login()
        self.loginVista.home.home.loginCode.setText("")
        self.loginVista.home.home.loginCode_2.setText("")
        if ingreso == True:
            self.ir_usuarios(self.loginVista.home)
        elif ingreso == False:
            self.ir_habitaciones(self.loginVista.home)
        else:
            self.loginVista.home.home.loginCode.setStyleSheet(
                "border-radius: 10px; border: 2px solid red; font: 24px; background-color: white;")
            self.loginVista.home.home.loginCode_2.setStyleSheet(
                "border-radius: 10px; border: 2px solid red; font: 24px; background-color: white;")
            self.loginVista.home.home.nombre_Inc.show()
            self.loginVista.home.home.contrasena_Inc.show()
        
    def ir_usuarios(self,de):
        de.close()
        self.usuariosVista.usuarios.show()
        self.usuariosVista.showUsers()
        self.habitacionesVista.showRooms()
    
    def ir_login(self,de):
        de.close()
        globales.Usuario = None
        globales.Usuarios = []
        globales.Habitaciones = []
        globales.Dispositivos = []
        globales.Habitacion = None
        self.loginVista.home.show()

    def ir_habitaciones(self, de):
        de.close()
        globales.Habitaciones = self.habitacionesVista.habitacionC.obtener_Habitaciones()
        self.habitacionesVista.habitaciones.show()
        self.habitacionesVista.showRooms()
        self.habitacionesVista.showDevices()

        
