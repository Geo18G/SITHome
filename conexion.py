import pymysql
class Conexion:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='sithome'
        )
        self.cursor = self.connection.cursor()
        print("conexion correcta")

    def close(self):
        self.connection.close()
        print("conexion a base de datos cerrada")