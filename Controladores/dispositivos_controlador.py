
from conexion import Conexion


class DispositivoControlador:
    def __init__(self):
        self.__conexion = Conexion()

    def crearDispositivo(self,dispositivo):
        sql = f"INSERT INTO dispositivos (iddispositivos, nombre, estado, habitaciones_idhabitaciones) " \
              f"VALUES (NULL, '{dispositivo.getNombreD()}','{dispositivo.getStatus()}','{dispositivo.getHabitacionD()}')"
        return self.__conexion.insert(sql)

    def actualizarDispositivo(self,dispositivo,id):
        sql = f"UPDATE dispositivos SET nombre ='{dispositivo.getNombreD()}',estado ='{dispositivo.getStatus()}'," \
              f"habitaciones_idhabitaciones ='{(dispositivo.getHabitacionD())}' WHERE iddispositivos = '{id}'"
        return self.__conexion.update(sql)

    def eliminarDispositivo(self,id):
        sql = f"DELETE FROM dispositivos WHERE iddispositivos = '{id}'"
        return self.__conexion.delete(sql)

    def eliminarDispositivosPorHab(self,idH):
        sql = f"DELETE FROM dispositivos WHERE habitaciones_idhabitaciones = '{idH}'"
        return self.__conexion.delete(sql)

    def mostrarDispositivos(self,idH):
        sql = f"SELECT iddispositivos, nombre, estado FROM dispositivos WHERE habitaciones_idhabitaciones = '{idH}'"
        return self.__conexion.selectAll(sql)

    def obtenerStatus(self,id):
        sql = f"SELECT estado FROM dispositivos WHERE iddispositivos = '{id}'"
        return self.__conexion.select(sql)

    def cambiarStatus(self, id, estado):
        sql = f"UPDATE dispositivos SET estado = '{estado}' WHERE iddispositivos = '{id}'"
        return self.__conexion.update(sql)


