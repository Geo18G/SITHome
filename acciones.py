from Vistas.login_vista import LoginVista
from Vistas.usuarios_vista import UsuariosVista
from Vistas.habitaciones_vista import HabitacionesVista
# from Vistas.dispositivos_vista import DispositivoVista
import globales

class Acciones():
    def __init__(self):
        self.loginVista = LoginVista()
        self.usuariosVista = UsuariosVista()
        self.habitacionesVista = HabitacionesVista()
        # self.dispositivosVista = DispositivoVista()
        self.inicializarWidgets()
        
    def inicializarWidgets(self):
        #Inicializacion de variables globales
        globales.Usuario = []
        globales.Habitaciones = []
        globales.Usuarios = []
        globales.Dispositivos = []
        globales.Contador = 0 
        globales.Condicion = True
        
        #Inicializacion de botones inactivos
        self.usuariosVista.usuarios.usuarios.registerButton.setEnabled(False)
        self.habitacionesVista.addH.uiForm.btn_crear.setEnabled(False)
        self.habitacionesVista.addH.uiForm.btn_guardar.setEnabled(False)
        self.habitacionesVista.addD.uiFormD.btn_registrar.setEnabled(False)
        self.habitacionesVista.addD.uiFormD.btn_guardar.setEnabled(False)
        self.usuariosVista.usuarios.usuarios.addUser.hide()
        self.usuariosVista.usuarios.usuarios.btnGuardar.hide()
        
        #Asignar funciones a botones de eventos
        #Usuarios
        self.usuariosVista.usuarios.usuarios.registerButton.clicked.connect(self.usuariosVista.SITHome_register)
        self.usuariosVista.usuarios.usuarios.viewPass.clicked.connect(self.usuariosVista.viewPass)
        self.usuariosVista.usuarios.usuarios.btnGuardar.clicked.connect(self.usuariosVista.editarUsuario)
        self.usuariosVista.usuarios.usuarios.addUser.clicked.connect(self.usuariosVista.ventanaUsuarioNormal)
        #Habitaciones
        self.habitacionesVista.habitaciones.habitaciones.addHabitacion.clicked.connect(lambda: self.habitacionesVista.mostrar_ventana_crear())
        self.habitacionesVista.habitaciones.habitaciones.addDispositivo.clicked.connect(lambda: self.habitacionesVista.mostrar_ventana_crearD())
        #Formulario habitaciones
        self.habitacionesVista.addH.uiForm.btn_guardar.clicked.connect(lambda: self.habitacionesVista.editarH())
        self.habitacionesVista.addH.uiForm.btn_crear.clicked.connect(lambda: self.habitacionesVista.addRoom())
        self.habitacionesVista.addH.uiForm.btn_cancelar.clicked.connect(lambda: self.habitacionesVista.addH.close())
        #Formulario dispositivos
        self.habitacionesVista.addD.uiFormD.btn_cancelar.clicked.connect(lambda: self.habitacionesVista.addD.close())
        self.habitacionesVista.addD.uiFormD.btn_registrar.clicked.connect(lambda: self.habitacionesVista.addDevice())
        self.habitacionesVista.addD.uiFormD.btn_guardar.clicked.connect(lambda: self.habitacionesVista.editarD())
        
        #Asignar funciones por cambio de eventos
        #Usuarios
        self.usuariosVista.usuarios.usuarios.nameRegister.textChanged.connect(lambda: self.usuariosVista.habilitarBtn(self.usuariosVista.usuarios.usuarios.registerButton))
        self.usuariosVista.usuarios.usuarios.codeRegister.textChanged.connect(lambda: self.usuariosVista.habilitarBtn(self.usuariosVista.usuarios.usuarios.registerButton))
        self.usuariosVista.usuarios.usuarios.nameRegister.textChanged.connect(lambda: self.usuariosVista.habilitarBtn(self.usuariosVista.usuarios.usuarios.btnGuardar))
        self.usuariosVista.usuarios.usuarios.codeRegister.textChanged.connect(lambda: self.usuariosVista.habilitarBtn(self.usuariosVista.usuarios.usuarios.btnGuardar))
        #Formulario habitacion
        self.habitacionesVista.addH.uiForm.nameRegister.textChanged.connect(
            lambda: self.habitacionesVista.habilitarBtn(self.habitacionesVista.addH.uiForm.btn_crear, self.habitacionesVista.addH.uiForm.nameRegister))
        self.habitacionesVista.addH.uiForm.nameRegister.textChanged.connect(
            lambda: self.habitacionesVista.habilitarBtn(self.habitacionesVista.addH.uiForm.btn_guardar, self.habitacionesVista.addH.uiForm.nameRegister))
        #Formulario dispositivos
        self.habitacionesVista.addD.uiFormD.nameRegister.textChanged.connect(
            lambda: self.habitacionesVista.habilitarBtn(self.habitacionesVista.addD.uiFormD.btn_registrar, self.habitacionesVista.addD.uiFormD.nameRegister))
        self.habitacionesVista.addD.uiFormD.nameRegister.textChanged.connect(
            lambda: self.habitacionesVista.habilitarBtn(self.habitacionesVista.addD.uiFormD.btn_guardar, self.habitacionesVista.addD.uiFormD.nameRegister))
        
        
        