from plantilla import *


class Programa():
    def __init__(self):
        self.home = LoginUi()
        self.usuarios = UsuariosUi()
        self.habitaciones = HabitacionesUi()
        self.formularioH = FormularioH()
        self.formularioD = FormularioD()