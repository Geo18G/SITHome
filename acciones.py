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
        self.usuariosVista.usuarios.usuarios.registerButton.clicked.connect(lambda: self.usuariosVista.SITHome_register())
        self.usuariosVista.usuarios.usuarios.viewPass.clicked.connect(lambda: self.usuariosVista.viewPass())
        self.usuariosVista.usuarios.usuarios.btnGuardar.clicked.connect(self.usuariosVista.editarUsuario)
        self.usuariosVista.usuarios.usuarios.addUser.clicked.connect(self.usuariosVista.ventanaUsuarioNormal)
        # self.usuariosVista.usuarios.usuarios.dispButton.clicked.connect(self.usuariosVista.goToHabitacionesVista)
        #elements & functions----------------
        self.usuariosVista.usuarios.usuarios.registerButton.setEnabled(False)
        self.usuariosVista.usuarios.usuarios.nameRegister.textChanged.connect(lambda: self.usuariosVista.habilitarBtn(self.usuariosVista.usuarios.usuarios.registerButton))
        self.usuariosVista.usuarios.usuarios.codeRegister.textChanged.connect(lambda: self.usuariosVista.habilitarBtn(self.usuariosVista.usuarios.usuarios.registerButton))
        self.usuariosVista.usuarios.usuarios.nameRegister.textChanged.connect(lambda: self.usuariosVista.habilitarBtn(self.usuariosVista.usuarios.usuarios.btnGuardar))
        self.usuariosVista.usuarios.usuarios.codeRegister.textChanged.connect(lambda: self.usuariosVista.habilitarBtn(self.usuariosVista.usuarios.usuarios.btnGuardar))
        self.usuariosVista.usuarios.usuarios.addUser.hide()
        self.usuariosVista.usuarios.usuarios.btnGuardar.hide()




        self.habitacionesVista.habitaciones.habitaciones.addHabitacion.clicked.connect(lambda: self.habitacionesVista.mostrar_ventana_crear())
        self.habitacionesVista.addH.uiForm.btn_cancelar.clicked.connect(lambda: self.habitacionesVista.addH.close())
        self.habitacionesVista.addD.uiFormD.btn_cancelar.clicked.connect(lambda: self.habitacionesVista.addD.close())
        self.habitacionesVista.addH.uiForm.btn_crear.setEnabled(False)
        self.habitacionesVista.addH.uiForm.btn_guardar.setEnabled(False)
        self.habitacionesVista.addD.uiFormD.btn_registrar.setEnabled(False)
        self.habitacionesVista.addD.uiFormD.btn_guardar.setEnabled(False)
        self.habitacionesVista.addH.uiForm.nameRegister.textChanged.connect(
            lambda: self.habitacionesVista.habilitarBtn(self.habitacionesVista.addH.uiForm.btn_crear, self.habitacionesVista.addH.uiForm.nameRegister))
        self.habitacionesVista.addH.uiForm.nameRegister.textChanged.connect(
            lambda: self.habitacionesVista.habilitarBtn(self.habitacionesVista.addH.uiForm.btn_guardar, self.habitacionesVista.addH.uiForm.nameRegister))
        self.habitacionesVista.addD.uiFormD.nameRegister.textChanged.connect(
            lambda: self.habitacionesVista.habilitarBtn(self.habitacionesVista.addD.uiFormD.btn_registrar, self.habitacionesVista.addD.uiFormD.nameRegister))
        self.habitacionesVista.addD.uiFormD.nameRegister.textChanged.connect(
            lambda: self.habitacionesVista.habilitarBtn(self.habitacionesVista.addD.uiFormD.btn_guardar, self.habitacionesVista.addD.uiFormD.nameRegister))
        self.habitacionesVista.addH.uiForm.btn_guardar.clicked.connect(lambda: self.habitacionesVista.editarH())
        self.habitacionesVista.addH.uiForm.btn_crear.clicked.connect(lambda: self.habitacionesVista.addRoom())
        self.habitacionesVista.addD.uiFormD.btn_registrar.clicked.connect(lambda: self.habitacionesVista.addDevice())
        self.habitacionesVista.addD.uiFormD.btn_guardar.clicked.connect(lambda: self.habitacionesVista.editarD())
        self.habitacionesVista.habitaciones.habitaciones.addDispositivo.clicked.connect(lambda: self.habitacionesVista.mostrar_ventana_crearD())