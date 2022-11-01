

import pymysql


class DispositivosControlador:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='sithome'
        )
        self.cursor = self.connection.cursor()

    def crearDispositivos(self):
        pass

    def actualizarDispositivos(self):
        pass

    def eliminarDispositivos(self):
        pass

    def mostrarDispositivos(self):
        pass
