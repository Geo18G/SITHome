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




        self.habitacionesVista.habitaciones.addHabitacion.clicked.connect(lambda: self.habitacionesVista.mostrar_ventana_crear())
        self.addH.uiForm.btn_cancelar.clicked.connect(lambda: self.addH.close())
        self.addD.uiFormD.btn_cancelar.clicked.connect(lambda: self.addD.close())
        self.addH.uiForm.btn_crear.setEnabled(False)
        self.addH.uiForm.btn_guardar.setEnabled(False)
        self.addD.uiFormD.btn_registrar.setEnabled(False)
        self.addD.uiFormD.btn_guardar.setEnabled(False)
        self.addH.uiForm.nameRegister.textChanged.connect(
            lambda: self.habilitarBtn(self.addH.uiForm.btn_crear, self.addH.uiForm.nameRegister))
        self.addH.uiForm.nameRegister.textChanged.connect(
            lambda: self.habilitarBtn(self.addH.uiForm.btn_guardar, self.addH.uiForm.nameRegister))
        self.addD.uiFormD.nameRegister.textChanged.connect(
            lambda: self.habilitarBtn(self.addD.uiFormD.btn_registrar, self.addD.uiFormD.nameRegister))
        self.addD.uiFormD.nameRegister.textChanged.connect(
            lambda: self.habilitarBtn(self.addD.uiFormD.btn_guardar, self.addD.uiFormD.nameRegister))
        self.addH.uiForm.btn_guardar.clicked.connect(lambda: self.editarH())
        self.addH.uiForm.btn_crear.clicked.connect(lambda: self.addRoom())
        self.addD.uiFormD.btn_registrar.clicked.connect(lambda: self.addDevice())
        self.addD.uiFormD.btn_guardar.clicked.connect(lambda: self.editarD())
        self.habitacion.habitaciones.addDispositivo.clicked.connect(lambda: self.mostrar_ventana_crearD())