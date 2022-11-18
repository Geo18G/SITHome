from acciones import Acciones


class Rutas(Acciones):
    def __init__(self):
        super(Rutas, self).__init__()
        
    def asignarRutas(self):
        self.loginVista.home.home.login.clicked.connect(lambda: self.ingresar())
    
    
    def ingresar(self):
        ingreso = self.loginVista.SITHome_Login()
        if ingreso == True:
            pass
        else:
            pass