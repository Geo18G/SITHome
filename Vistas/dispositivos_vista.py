

from PyQt5.QtWidgets import *
from interfaces.DevicesUi import Ui_SITHome_Dispositivos



class DispositivosUi(QMainWindow):
    def __init__(self):
        super(DispositivosUi, self).__init__()
        self.listaDispositivos = Ui_SITHome_Dispositivos()
        self.listaDispositivos.setupUi(self)
        # self.loginAdmin = UsuariosUi()
    #     self.inicialize()
    #
    #
    #     #
    # def inicialize(self):
    # #botones SIT--------------------------------------------------------------------------
    #     # self.loginAdmin.loginAdmin.dispButton.clicked.connect(lambda: self.allDevs())
    #
    #     # self.checkStatus('Puerta')
    #     # self.checkStatus('Luz')
    #
    #     # DispositivosUi().listaDispositivos.doorSwitch.clicked.connect(lambda: self.changeStatus('Puerta'))
    #     # DispositivosUi().listaDispositivos.lightSwitch.clicked.connect(lambda: self.changeStatus('Luz'))
    #     DispositivosUi().listaDispositivos.back.clicked.connect(lambda: DispositivosUi().hide())
    #     DispositivosUi().listaDispositivos.back.clicked.connect(lambda: self.loginAdmin.show())


    # def allDevs(self):
    #     # self.checkStatus("Puerta")
    #     # self.checkStatus("Luz")
    #     # self.loginAdmin.hide()
    #     DispositivosUi().show()

#         def checkStatus(self, device):
#             off = "assets\interruptor-off.png"
#             on = "assets\interruptor-on.png"
#             if device == "Puerta":
#                 devicePointer = self.devices.ui.doorSwitch
#             elif device == "Luz":
#                 devicePointer = self.devices.ui.lightSwitch
#             status = DB.database.checkStatusDB(device)
#             if status == 'ON':
#                 devicePointer.setIcon(QtGui.QIcon(on))
#             elif status == 'OFF':
#                 devicePointer.setIcon(QtGui.QIcon(off))
#
#         def changeStatus(self, device):
#             DB.database.changeStatusDB(device)
#             self.checkStatus(device)
# #