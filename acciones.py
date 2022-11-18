from Vistas.login_vista import LoginVista
from Vistas.usuarios_vista import UsuariosVista
from Vistas.habitaciones_vista import HabitacionesVista
import globales

class Acciones():
    def __init__(self):
        self.loginVista = LoginVista()
        self.usuariosVista = UsuariosVista()
        self.habitacionesVista = HabitacionesVista()
        self.inicializarWidgets()
        
    def inicializarWidgets(self):
        self.loginVista.home.home.login.clicked.connect(lambda: self.loginVista.SITHome_Login())
        globales.Usuario = None
        globales.idHabitaciones = None