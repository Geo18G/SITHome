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
        globales.Usuario = None
        globales.idHabitaciones = None
        
#buttons-------------
        self.usuariosVista.usuarios.usuarios.registerButton.clicked.connect(lambda: self.SITHome_register())
        self.usuariosVista.usuarios.usuarios.viewPass.clicked.connect(lambda: self.viewPass())
        self.usuariosVista.usuarios.usuarios.btnGuardar.clicked.connect(self.editarUsuario)
        self.usuariosVista.usuarios.usuarios.addUser.clicked.connect(self.ventanaUsuarioNormal)
        self.usuariosVista.usuarios.usuarios.dispButton.clicked.connect(self.goToHabitacionesVista)
        #elements & functions----------------
        self.usuariosVista.usuarios.usuarios.registerButton.setEnabled(False)
        self.usuariosVista.usuarios.usuarios.nameRegister.textChanged.connect(lambda: self.habilitarBtn(self.usuarios.usuarios.registerButton))
        self.usuariosVista.usuarios.usuarios.codeRegister.textChanged.connect(lambda: self.habilitarBtn(self.usuarios.usuarios.registerButton))
        self.usuariosVista.usuarios.usuarios.nameRegister.textChanged.connect(lambda: self.habilitarBtn(self.usuarios.usuarios.btnGuardar))
        self.usuariosVista.usuarios.usuarios.codeRegister.textChanged.connect(lambda: self.habilitarBtn(self.usuarios.usuarios.btnGuardar))
        self.usuariosVista.usuarios.usuarios.addUser.hide()
        self.usuariosVista.usuarios.usuarios.btnGuardar.hide()